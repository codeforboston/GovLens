import csv, os, json, boto3, asyncio

# The Scheduler will invoke this function. Parameter is list of agencies for which the data needs to be scraped

class ScraperService:
    def __init__(self):
        # self.boto3client = boto3.client('lambda', aws_access_key_id="AKIA4CRG6M6VMNCDB6B7",
        #                                aws_secret_access_key="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", region_name='us-east-2')
    
        self.boto3client = boto3.client('lambda', aws_access_key_id="AKIAUSPQNXEUFQ7NFVPB",
                                        aws_secret_access_key="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", region_name='us-east-1')

    async def scrape_data(self, agencies):
        if len(agencies) <= 0:
            print("No Agency information was passed to scrape")
            return
        else:
            try:
                agency_info_request = {}
                agency_info_request['agencies'] = agencies
                json_request = json.dumps(agency_info_request)
                print(f"{json.dumps(json_request[0])}")
                self.boto3client.invoke(FunctionName='scrapers', InvocationType='Event', Payload=json_request)
                print(f"Completed posting the agency information")
            except Exception as ex:
                print(f"Error while posting the agency information to lambda: {str(ex)}")
                return []


