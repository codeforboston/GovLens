
Scraper scrapes the agency information and posts the information to the Django API. 
scrape_handler.py is the entry point for scraping. 
when we run from our local machine, we get the list of agencies and start scraping them. 
But when deployed to AWS, the scraper is invoked by the schedule and scrape_data is the method hooked up to the lambda.

if running from local, python scraper.py should run the scraper. make sure to set the environment variable to your local endpoint.

Pushing it to AWS lambda:
1) zip the scraper folder.
2) go to AWS lamba and upload the zipped folder https://console.aws.amazon.com/lambda/home?region=us-east-1#/functions
3) test the lambda by using this json 
4) confirm that there are no errors by looking at cloudwatch logs. https://console.aws.amazon.com/cloudwatch/home?region=us-east-1#logStream:group=/aws/lambda/scrapers;streamFilter=typeLogStreamPrefix 
