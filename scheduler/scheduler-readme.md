Scheduler working:

Scheduler reads the list of the agencies from Django API (Govlens API) and then calls the Lambda function which scrapes the websites.
job_config.json contains all the configuration for the scheduler.
We need to provide the following information in the configuration
    a) Schedule start time: At what time the schedule should start every week. 
    b) "agency_batch_size" -- The number of agencies we should scrape at a time. It depends on how the lambda performs. If lambda can scrape 100's of websites at a time,
    the number can be 100. 
    c) "interval_between_runs_seconds" -- The number of seconds we have in between the scheduled runs. For example, we send the request to scrape 100 websites and then wait  
    for 10 minutes before scraping the next 100 websites.

Currently the website gets the data from "http://govlens.us-east-2.elasticbeanstalk.com/api/agencies/"

scrape_data sends the request to the lambda function. The credentials for the lambda function should be stored as environment variables and used here. 

        self.boto3client = boto3.client('lambda', aws_access_key_id="",aws_secret_access_key="", region_name='')  (make sure we have the proper credentials for accessing the AWS lambda) 

Instructions for running in EC2 instance. (all the below needs to be automated. A person with some AWS experience will find these steps elementary)
1) After you make some changes to the scheduler, we need to push the image to amazon's registry.
Get the AWS keys for aws_access_key_id and aws_secret_access_key and store it in (~/.aws) in a file named "credentials"
2) login into ECR (Elastic Container Registry). aws ecr get-login --region us-east-1
3) Build the docker image and the important point is image needs to be tagged. The image should be tagged with the repository name in ECR. 
   That's how Amazon determines the repo for the image you post. 
   this is the link for ECR. https://console.aws.amazon.com/ecr/repositories?region=us-east-1
   For each image, you will be able to see the URI. the URI looks like this dummy.dkr.ecr.us-east-1.amazonaws.com/scheduler (replace dummy with the actual ID)
   you need to tag the image with the URI. for example, it looks something like this. docker build . -t dummy.dkr.ecr.us-east-1.amazonaws.com/scheduler:v5 
   (remember to give a version number which doesn't already exist there in ECR. Otherwise it gives an error when you try to push the image to ECR)
   after the image is built, you can push the image using the command docker push dummy.dkr.ecr.us-east-1.amazonaws.com/scheduler:v5 
4) If you refresh the ECR page, you should see the latest version there. 
5) login into the ECR instance ssh -i test-pem.pem ec2-user@(actual ip).compute-1.amazonaws.com
6) docer pull the latest image (which we just pushed) and run the image. The scheduler will start scraping the websites from (time specified in job_config.json file)


