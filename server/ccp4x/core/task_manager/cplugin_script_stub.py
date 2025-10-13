from typing import Optional, Any, Dict, List

# Stub implementation of CPluginScript for CCP4i2 modern Python


class CPluginScript:
    # Class-wide attributes (can be set by subclasses)
    TASKNAME: Optional[str] = None
    TASKVERSION: Optional[str] = None
    TASKMODULE: Optional[str] = None
    TASKTITLE: Optional[str] = None
    DESCRIPTION: Optional[str] = None
    MAINTAINER: Optional[str] = None
    TASKCOMMAND: Optional[str] = None
    SUBTASKS: Optional[List[str]] = None
    COMTEMPLATE: Optional[str] = None
    COMTEMPLATEFILE: Optional[str] = None
    COMLINETEMPLATE: Optional[str] = None
    INTERRUPTABLE: Optional[bool] = None
    RESTARTABLE: Optional[bool] = None
    INTERRUPTLABEL: Optional[str] = None
    DBOUTPUTDATA: Optional[List[str]] = None
    ASYNCHRONOUS: Optional[bool] = None
    PERFORMANCECLASS: Optional[str] = None
    RUNEXTERNALPROCESS: Optional[bool] = True
    CLONEABLE: Optional[bool] = True
    ERROR_CODES: Dict[int, Dict[str, Any]] = {}
    PURGESEARCHLIST: Optional[List] = None

    # Status flags
    SUCCEEDED = "SUCCEEDED"
    FAILED = "FAILED"
    UNSATISFACTORY = "UNSATISFACTORY"
    INTERRUPTED = "INTERRUPTED"

    def __init__(self, parent=None, name=None, workDirectory=None):
        self.parent = parent
        self.name = name
        self.workDirectory = workDirectory
        self.container = None  # Should be a CContainer instance
        self.errorReport = None  # Should be a CErrorReport instance
        self.commandLine = []
        self.commandScript = []
        self.is_async = False
        self.timeout = None
        self.runningProcessId = None

    def makePluginObject(self, pluginName: str, reportToDatabase: bool = True):
        """Create an instance of a CPluginScript subclass."""
        pass

    def loadContentsFromXml(self, xmlFile: str):
        """Set the contents of the container from the DEF file."""
        pass

    def checkInputData(self) -> List[str]:
        """Check that input files exist. Return list of missing files."""
        return []

    def checkOutputData(self, container=None):
        """Provide output file names if missing."""
        pass

    def appendErrorReport(
        self,
        code: int,
        details: Optional[str] = None,
        name: Optional[str] = None,
        cls: Optional[Any] = None,
    ):
        """Append an error description to the error report."""
        pass

    def extendErrorReport(self, other):
        """Append errors from another error report object."""
        pass

    def appendCommandLine(self, *args):
        """Append words to the command line."""
        self.commandLine.extend(args)

    def appendCommandScript(self, text):
        """Add a line to the command script."""
        self.commandScript.append(str(text))

    def writeCommandFile(self):
        """Write the command script to a file."""
        pass

    def makeFileName(
        self, format: str, ext: Optional[str] = None, baseName: Optional[str] = None
    ) -> str:
        """Generate an appropriate file name."""
        return ""

    def process(self):
        """Run the main process."""
        return self.SUCCEEDED

    def makeCommandAndScript(self):
        """Create command line and script."""
        pass

    def startProcess(self, command: Optional[str] = None, reportStatus: bool = True):
        """Start external process."""
        return self.SUCCEEDED

    def postProcess(self, processId: Optional[int] = None, data: Optional[Any] = None):
        """Called after process finishes."""
        pass

    def postProcessWrapper(self, finishStatus: str):
        """Clean up after last wrapper plugin."""
        pass

    def reportStatus(self, finishStatus: str):
        """Report completion to database, write PARAMS file, emit signal."""
        pass

    def postProcessCheck(self, processId: Optional[int] = None):
        """Query process manager for job status."""
        return self.SUCCEEDED

    def logFileText(self) -> str:
        """Return the text of a log file."""
        return ""

    def updateJobStatus(
        self, status: Optional[str] = None, finishStatus: Optional[str] = None
    ):
        """Report job status to database."""
        pass

    def saveParams(self):
        """Save the content of self.container to a PARAMS file."""
        pass

    def getProcessId(self) -> Optional[int]:
        """Return the processId."""
        return self.runningProcessId

    def joinMtz(self, outFile: str, inFiles: List[List[str]]):
        """Join multiple MTZs into one MTZ."""
        pass

    def splitMtz(self, inFile: str, outFiles: List[List[str]]):
        """Split one MTZ into multiple MTZs."""
        pass

    # Mini-MTZ helpers
    def makeHklin(self, miniMtzsIn=None, hklin=None):
        pass

    def splitHklout(
        self, miniMtzsOut=None, programColumnNames=None, inFile=None, logFile=None
    ):
        pass

    def splitHkloutList(
        self,
        miniMtzsOut=None,
        programColumnNames=None,
        outputBaseName=None,
        outputContentFlags=None,
        inFileList=None,
        logFile=None,
    ):
        pass

    # Interrupt/restart helpers
    def testForInterrupt(self) -> bool:
        return False

    # Project defaults
    def getProjectDefaultParameters(self, taskName: str, paramsList: List[str]):
        pass

    def saveProjectDefaultParameters(self, defaultsContainer):
        pass

    def loadProjectDefaults(self):
        pass

    # Export helpers
    @staticmethod
    def exportJobFileMenu(jobId):
        pass

    @staticmethod
    def exportJobFile(jobId, mode):
        pass

    # File cleanup
    def purgeFiles(self):
        pass

    # Signal helpers
    def connectSignal(self, plugin, signal, handler):
        pass

    # Data movement
    def copyData(self, otherContainer, dataList=None):
        pass

    # For Qt compatibility (stub)
    def setFinishHandler(self, handler):
        pass

    # For async pipelines
    def setWaitForFinished(self, timeout):
        pass

    # For testing
    @staticmethod
    def TESTSUITE():
        pass

    @staticmethod
    def testModule():
        pass

    # Add any other externally called methods as needed
