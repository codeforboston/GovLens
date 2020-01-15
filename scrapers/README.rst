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

Requirements
============

Google Lighthouse API Key
~~~~~~~~~~~~~~~~~~~~~~~~~
Get the API key for accessing lighthouse from here: https://developers.google.com/speed/docs/insights/v5/get-started (click on the button get key)

Put that key in GOOGLE_API_KEY environment variable.

Running the Scrapers
====================
``scrape_handler.py`` is the entry point for scraping.
When we run from our local machine, we get the list of agencies and start scraping them.
But when deployed to AWS, the scraper is invoked by the schedule and ``scrape_handler.scrape_data()`` is the method hooked up to the lambda.

Local
~~~~~
If running from local, the following command should run the scraper::

  python scraper.py

Make sure to set the environment variable to your local endpoint.

AWS Lambda
~~~~~~~~~~
Pushing it to AWS lambda:
1) zip the ``scraper/`` folder.
2) go to AWS lamba and upload the zipped folder: https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions
3) test the lambda by using this json (??)
4) confirm that there are no errors by looking at cloudwatch logs: https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logStream:group=/aws/lambda/scrapers;streamFilter=typeLogStreamPrefix
