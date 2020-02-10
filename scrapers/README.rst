``scrapers``
------------

Description
===========
Code related to scripts, "scrapers", which scrape the agency information and post the information to the Django API.

Directory Structure
===================

::

  ├── agency_api_service.py         - connects to GovLens API for agency info
  ├── agency_dataaccessor.py        - read/write to/from database containing scraped info
  ├── lighthouse.py                 - connects to Google Lighthouse API
  ├── process_agency_info.py        - connects to an agency site & runs scrapers
  ├── README.rst                    - this file!
  ├── scrape_handler.py             - **Start here!** Starts API services and maps to agency processors.
  ├── urls.json                     - list of URLS pointing to government sites
  ├── data/
  │   └── agencies.csv              - spreadsheet containing scraped information (match of Google Sheets?)
  └── scrapers/
      ├── __init__.py
      ├── accessibility_scraper.py  - scrapes for multi-language, performance, mobile-bility
      ├── base_api_client.py
      ├── base_scraper.py           - base class for scrapers to inherit
      ├── security_scraper.py       - scrapes for HTTPS & privacy policy
      └── social_scraper.py         - scrapes for phone number, email, address, social media

Quick Start
===========

Configuration
~~~~~~~~~~~~~

There are a few required environmental variables. The easiest way to set them in development is to create a file called `.env` in the root directory of this repository (don't commit this file). The file (named `.env`) should contain the following text::

    GOVLENS_API_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
    GOVLENS_API_ENDPOINT=http://127.0.0.1:8000/api/agencies/
    GOOGLE_API_TOKEN=XXXXXXXXXXXXXXXXXXXXXXXX

To get the ``GOOGLE_API_TOKEN``, you need to visit the following page: https://developers.google.com/speed/docs/insights/v5/get-started

To get the ``GOVLENS_API_TOKEN``, run ``python3 manage.py create_scraper_user``. Copy the token from the command output and paste it into the ``.env`` file.

Execution
~~~~~~~~~

Once you have created the `.env` file as mentioned above, run the scraper::

  # run the following from the root directory of the repository
  python3 -m scrapers.scrape_handler

Design
======

The scraper is intended to be used both locally and on AWS Lambda.

The ``scrapers`` directory in the root of this repository is the top-level Python package for this project. This means that any absolute imports should begin with ``scrapers.MODULE_NAME_HERE``.

``scrapers/scrape_handler.py`` is the main Python module invoked. On AWS Lambda, the method ``scrape_handler.scrape_data()`` is imported and called directly.

AWS Lambda
~~~~~~~~~~
Pushing it to AWS lambda:

1. zip the ``scraper/`` folder.
2. go to AWS lamba and upload the zipped folder: https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions
3. test the lambda by using this json (??)
4. confirm that there are no errors by looking at cloudwatch logs: https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logStream:group=/aws/lambda/scrapers;streamFilter=typeLogStreamPrefix
