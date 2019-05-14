# Civic Pulse

## Installation instructions

Clone the repository:

```bash
git clone git@github.com:codeforboston/civicpulse.git
```

Navigate to the base directory of the reposistory and prepare to install depedencies.

To start, it is recommend to create a
[virtual environment](https://virtualenv.pypa.io/en/stable/userguide/). If you have not
used `virtualenv` before, install it with: `pip install virtualenv`.

```bash
# Create a virtual environment to manage dependencies
virtualenv venv
source venv/bin/activate
```

Now install the dependencies with pip:

```bash
# Install requirements.txt
pip install -r requirements.txt
```

After the dependencies have installed, we want to prepare the database.

```bash
# Perform data migrations
python manage.py migrate
```

Then, we need to import a CSV file containing existing agency information. Start by
running a Django shell:

```bash
python manage.py shell

# From within the shell
>>> from apps.civic_pulse.utils.load_models import *
>>> fill_agency_objects()
```

Finally, the database is ready to go! We are now ready to run the server:

```bash
python manage.py runserver
```

Navigate in your browser to `http://127.0.0.1:8000/` and you should see a list of
agencies.
