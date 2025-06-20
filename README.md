# ccp4i2-django

## Development

Clone the project from GitHub,
install the dependencies, make an inital database migration
and start the Django development server for the REST API.
ccp4i2-django is an overlay on vanilla ccp4i2, but requires some python dependencies of CCP4 to be updated.  
For development, therefore, the currently supported mechanism
is to install a dedicated instance of ccp4 in which those dependencies can be updated without risk to the developer's main CCP4 installation.

```console
user:$$ # After installing or activating your dedicated CCP4 instance and
user:~$ git clone https://github.com/paulsbond/ccp4i2-django
user:~$ cd ccp4i2-django/server
user:~/ccp4i2-django/server$ ccp4-python -m pip install --editable .
user:~/ccp4i2-django/server$ ccp4-python manage.py migrate
user:~/ccp4i2-django/server$ ccp4-python manage.py runserver
```

There should now be a browsable API with autogenerated forms
at http://localhost:8000.

## Install and import test suite

The ccp4i2 test suite can be used to provide substrate for development
To recover and import the test suite, navigate to the directory in which you have installed ccp4i2-django:

```console
user:~/ccp4i2-django/server$ #Starting from the directory where you ended up above
user:~/ccp4i2-django/server$ cd ../..
user:~$ git clone git@gitlab.com:ccp4i2/test101.git
user:~$ cd ccp4i2-django/server
user:~$ ccp4-python manage.py import_ccp4_project_zip ../../test101/ProjectZips/*.ccp4_project.zip
```

## Setup and run client

For easy viewing of the REST API and Next.js logs separately,
start the Next.js development server in a new terminal. Moorhen is now loaded with
ccp4i2-django, and this means an extra installment step is needed to copy the Moorhen web assembly
and other resources into the `public' folder of the ccp4i2-django NextJS app.

```console
user:~$ cd ccp4i2-django/client
user:~/ccp4i2-django/client$ npm ci
user:~/ccp4i2-django/client$ cp -r node_modules/moorhen/public/* ./public/
user:~/ccp4i2-django/client$ npm run dev
```

Open a browser at http://localhost:3000 to view the app.
The Django server and the Next.js server
will both automatically restart
when any changes are made to files.

If making any changes to the database models,
run the following commands to update the database
then restart the server:

```console
user:~/ccp4i2-django$ python manage.py makemigrations
user:~/ccp4i2-django$ python manage.py migrate
```
