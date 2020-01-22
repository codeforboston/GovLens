import json

import boto3


class ScraperService:
    def __init__(self):
        #  fill in the information with correct credentials
        self.boto3client = boto3.client(
            "lambda", aws_access_key_id="", aws_secret_access_key="", region_name=""
        )

    async def scrape_data(self, agencies):
        if len(agencies) <= 0:
            print("No Agency information was passed to scrape")
            return
        else:
            try:
                agency_info_request = {}
                agency_info_request["agencies"] = agencies
                json_request = json.dumps(agency_info_request)
                names = [o["name"] for o in agencies]
                print(f"Scraping for Agencies:  {json.dumps(names)}")
                self.boto3client.invoke(
                    FunctionName="scrapers",
                    InvocationType="Event",
                    Payload=json_request,
                )
                print(f"Completed invoking the lambda")
            except Exception as ex:
                print(f"Error while invoking the lambda: {str(ex)}")
                return []
