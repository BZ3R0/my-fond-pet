# My Fond Pet

My Fond Pet is a tool that provides some services to the pet public. These services include:

- Pets adoption collaborative tool.
- Missing pets disclosure collaborative tool.
- Marketplace for veterinary services and pet-shops.
- Adoption information blog.

### To generate database

The scripts for databases was made using SQLAlchemy. If you cloned the application for the first time, you must initialize and perform migration of the databases. For each change made in the databases, a migration and upgrade must be performed from the following commands:

```sh
$ python3 run.py db init
$ python3 run.py db stamp heads
$ python3 run.py db migrate
$ python3 run.py db upgrade
```

### To execute
If this is your first time running the application, you should create a python virtual environment and install the necessary packages. First of all you have to install virtualenv and then run the commands as follows:

```sh
# Install virutalenv on a linux so
$ sudo apt-get install virtualenv

# Create python virtual environment
$ virtualenv -p python3 .venv

# Initiate virtual environment
$ . .venv/bin/activate

# Install the respective application dependence
(.venv)$ .venv/bin/pip3 install -r requirements.txt
```

After that, you can run the application (make ensure that virtual environment is active) with the following command:

```sh
(.venv)$ python3 run.py runserver
```
