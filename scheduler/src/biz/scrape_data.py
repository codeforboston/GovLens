import csv, os, json, boto3, asyncio


class ScraperService:
    def __init__(self):
                #  fill in the information with correct credentials
        self.boto3client = boto3.client('lambda', aws_access_key_id="",aws_secret_access_key="",region_name="" )

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
                print(f"Completed invoking the lambda")
            except Exception as ex:
                print(f"Error while invoking the lambda: {str(ex)}")
                return []


