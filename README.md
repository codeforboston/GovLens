# Civic Pulse

## About the project

Civic Pulse is a project from [MuckRock](https://www.muckrock.com) and [Code for Boston](https://www.codeforboston.org). We scan thousands of government websites to check how well they stack up on security, accessibility, and public accountability. [You can join us every Tuesday night to help out](https://www.meetup.com/Code-for-Boston).

![A screenshot of what a Civic Scorecard looks like](README_images/scorecard.png )

## Getting started basics

- [ ] Make sure [you've registered for the Code for Boston Slack](https://communityinviter.com/apps/cfb-public/code-for-boston-slack-invite).
- [ ] Join the #MuckRock channel on Slack.
- [ ] Ask a current member to be added to our Github organization ([They'll need to click here](https://github.com/codeforboston/civicpulse/settings/collaboration)). After they've sent you an invite, you'll need to either check your email or notifications in Github (the alarm icon on the top right of your Github page) to accept the invite.
- [ ] If you're interested in working on the backend of the site, [try following the instructions](#installation-instructions)

## Project goals

The goal is to create an automatically updated database that tracks, over time, how well government agencies websites at the state, local, and federal levels follow best practices when it comes to HTTPS security, mobile friendliness, reader accessibility, and other key areas.

Over time, we hope to show whether both individual agencies are improving or worsening, as well as help highlight national shifts along the metrics we monitor. Individual pages show the most recent snapshot ranking, but our API will make historical data available.

## Current status

The project is currently in testing stages, as we work to both develop usable, accurate data and build a pipeline for regularly populating it. The site currently can run locally, but several of the data categories are filled with randomized testing data and any report cards generated are for **demonstration purposes only**. These scores do not represent actual scores for agencies.

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
>>> exit()
```

Finally, the database is ready to go! We are now ready to run the server:

```bash
python manage.py runserver
```

Navigate in your browser to `http://127.0.0.1:8000/` and you should see a list of
agencies.
