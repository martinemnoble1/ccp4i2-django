import uuid
from typing import List
import logging
import re
from core import CCP4File
from core import CCP4PerformanceData
from core import CCP4Data
from ccp4i2.core.CCP4Data import CList
from ccp4i2.core.CCP4Container import CContainer as CContainer
from ccp4i2.core.CCP4File import CDataFile as CDataFile
from ccp4i2.core.CCP4File import CI2XmlDataFile as CI2XmlDataFile
from ccp4i2.core.CCP4PerformanceData import CPerformanceIndicator
from ...db import models
from .find_objects import find_objects

logger = logging.getLogger(f"ccp4x:{__name__}")


def extract_from_first_bracketed(path: str) -> str:
    parts = path.split(".")
    for i, part in enumerate(parts):
        if re.search(r"\[.*\]", part):
            return ".".join(parts[i:])
    return parts[-1]  # fallback to the last part if no bracketed part found


def is_data_file(item):
    return isinstance(
        item,
        (
            CCP4File.CDataFile,
            CDataFile,
        ),
    )


def glean_job_files(
    jobId: str = None,
    container: CContainer = None,
    roleList: List[int] = [0, 1],
    unSetMissingFiles=True,
):
    """
    Gleans job files based on the provided job ID and container.

    This function retrieves a job object using the provided job ID, then finds
    and processes file objects based on the specified roles. It updates the job
    with input and output files and their uses, and gleans performance indicators
    from the output data.

    Args:
        jobId (str, optional): The UUID of the job as a string. Defaults to None.
        container (CContainer, optional): The container holding input and output data. Defaults to None.
        roleList (List[int], optional): A list of roles to process. Defaults to [0, 1].
        unSetMissingFiles (bool, optional): Flag to unset missing files. Defaults to True.

    Returns:
        None
    """
    job = models.Job.objects.get(uuid=uuid.UUID(jobId))
    print("Gleaning job %s", job)
    inputs: List[CDataFile] = find_objects(
        container.inputData,
        lambda a: is_data_file(a),
        True,
    )
    outputs: List[CDataFile] = find_objects(
        container.outputData,
        lambda a: is_data_file(a),
        True,
    )
    if models.FileUse.Role.OUT in roleList:
        make_files(job, outputs, unSetMissingFiles)
    if models.FileUse.Role.IN in roleList:
        make_file_uses(job, inputs)
    glean_performance_indicators(container.outputData, job)
    # the_plugin = get_job_plugin(job)
    # the_plugin.container = container
    # save_params_for_job(the_plugin, job, mode="PARAMS")


def make_files(
    job: models.Job, objects: List[CDataFile], unSetMissingFiles: bool = True
):
    for item in objects:
        if item.exists():
            logger.info("File for param %s exists=%s", item.objectName(), item.exists())
            _ = create_new_file(job, item)
            # create_file_use(job, item, the_file, role)
        elif unSetMissingFiles:
            item.unSet()


def create_new_file(job: models.Job, item: CDataFile):

    logger.info("Creating new file %s", item.objectName())
    file_type = item.qualifiers("mimeTypeName")
    if file_type is None or len(file_type.strip()) == 0:
        logger.error(
            "Class %s Does not have an associated mimeTypeName....ASK FOR DEVELOPER FIX",
            str(item.__class__),
        )
        file_type = "Unknown"
    elif file_type == "application/grace":
        file_type = "Unknown"
    elif file_type == "application/xml":
        file_type = "Unknown"
    try:
        file_type_object = models.FileType.objects.get(name=file_type)

    except models.FileType.DoesNotExist:
        logger.exception(
            "Could not find file type matching %s objectPath %s",
            file_type,
            item.objectName(),
        )
        return

    sub_type = getattr(item, "subType", None)
    try:
        sub_type = int(sub_type)
    except AttributeError as err:
        logger.debug(
            "No sub_type %s on %s",
            sub_type,
            item.baseName,
            exc_info=err,
        )
        sub_type = None

    content = getattr(item, "contentFlag", None)
    try:
        content = int(content)
    except AttributeError as err:
        logger.debug(
            "No content %s on %s",
            content,
            item.baseName,
            exc_info=err,
        )
        content = None
    annotation = getattr(item, "annotation", None)
    if annotation is not None:
        annotation = str(annotation)
    name = getattr(item, "baseName", None)
    if name is not None:
        name = str(name)
    job_param_name = extract_from_first_bracketed(item.objectPath())
    directory = 1

    try:
        try:
            the_file = models.File.objects.get(
                job=job, directory=directory, name=name, job_param_name=job_param_name
            )
            logger.error("Found identikit file %s %s", item.objectName(), the_file)
        except models.File.DoesNotExist:
            the_file = models.File(
                name=name,
                annotation=annotation,
                type=file_type_object,
                sub_type=sub_type,
                content=content,
                job=job,
                job_param_name=job_param_name,
                directory=directory,
            )

            the_file.save()
            item.dbFileId.set(str(the_file.uuid))
            logger.info("Created File for param %s", item.objectName())
    except Exception as err:
        logger.exception("Exception harvesting %s", job_param_name, exc_info=err)
    return the_file


def create_file_use(job: models.Job, item: CDataFile, the_file: models.File, role: int):
    try:
        job_param_name = extract_from_first_bracketed(item.objectPath())
        file_use = models.FileUse(
            file=the_file, job=job, job_param_name=job_param_name, role=role
        )
        file_use.save()
    except Exception as err:
        logger.exception(
            "Failed in making file use for %s job %s role %s",
            item.objectName(),
            job.number,
            role,
            exc_info=err,
        )
    logger.info("Created FileUse for param %s", job_param_name)


def make_file_uses(job: models.Job, item_dicts: List[CDataFile]):
    for item in item_dicts:
        role: int = models.FileUse.Role.IN
        file_uuid_member = getattr(item, "dbFileId", None)
        if file_uuid_member is None:
            continue
        else:
            file_uuid_str = str(file_uuid_member)
            if len(file_uuid_str.strip()) == 0:
                logger.info(
                    "dbFileId on parameter %s is zero length", item.objectName()
                )
                continue
            file_uuid = uuid.UUID(file_uuid_str)
        logger.debug(
            "objectName [%s] iSet[%s] exists[%s] uuid_str[%s]",
            item.objectName(),
            item.isSet(),
            item.exists(),
            file_uuid_str,
        )
        if item.isSet() and item.exists() and hasattr(item, "objectName"):
            the_file = models.File.objects.get(uuid=file_uuid)
            try:
                file_use = models.FileUse.objects.get(file=the_file, job=job, role=role)
                logging.error(
                    "In trying to save [%s %s %s %s] found existing FileUse [%s %s %s %s]",
                    the_file,
                    job,
                    role,
                    item.objectName(),
                    file_use.file,
                    file_use.job,
                    file_use.role,
                    file_use.job_param_name,
                )
            except models.FileUse.DoesNotExist:
                try:
                    job_param_name = extract_from_first_bracketed(item.objectPath())
                    fileUse: models.FileUse = models.FileUse(
                        file=the_file,
                        job=job,
                        role=role,
                        job_param_name=job_param_name,
                    )
                    logger.info("Created FileUse for parameter %s", job_param_name)
                    fileUse.save()
                except models.File.DoesNotExist as err:
                    logger.exception(
                        "Failed finding file for new file_use %s",
                        file_uuid,
                        exc_info=err,
                    )
                except Exception as err:
                    logger.exception(
                        "Different exception harvesting %s %s %s",
                        job.number,
                        role,
                        item.objectName(),
                        exc_info=err,
                    )


def glean_performance_indicators(container: CContainer, the_job: models.Job) -> None:
    kpis = find_objects(
        container,
        lambda a: isinstance(
            a,
            (
                CCP4PerformanceData.CPerformanceIndicator,
                CPerformanceIndicator,
            ),
        ),
        True,
    )
    for kpi in kpis:
        for kpi_param_name in kpi.dataOrder():
            value = getattr(kpi, kpi_param_name)
            if value is None:
                continue

            job_value_key, _ = models.JobValueKey.objects.get_or_create(
                name=str(kpi_param_name), defaults={"description": str(kpi_param_name)}
            )
            try:
                if isinstance(value, CCP4Data.CFloat):
                    model_class = models.JobFloatValue
                    value = float(value)
                elif isinstance(value, CCP4Data.CString) and len(str(value)) > 0:
                    model_class = models.JobCharValue
                    value = str(value)
                else:
                    continue
            except TypeError as err:
                logging.debug("Failed to glean value", exc_info=err)
                continue

            try:
                kpi_object = model_class(job=the_job, key=job_value_key, value=value)
                kpi_object.save()
            except TypeError as err:
                logger.exception(
                    "Failed saving value %s for key %s",
                    value,
                    kpi_param_name,
                    exc_info=err,
                )
