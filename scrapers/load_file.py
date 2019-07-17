import csv, os
import json

from process_agency_info import ProcessAgencyInfo

ID_ROW = 1
NAME_ROW = 2
PHONE_ROW = 5
BACKUP_PHONE_ROW = 6
WEBSITE_ROW = 8
TWITTER_ROW = 9
BACKUP_TWITTER_ROW = 10
FACEBOOK_ROW = 17


def fill_agency_objects(filepath=os.path.join(os.path.dirname(__file__),
                                              "./data/agencies.csv")):

    with open(filepath) as file:
        reader = csv.reader(file)
        next(reader, None)  # skip the headers

        i = 0
        all_agency_info=[]
        for row in reader:
            # only run 100 to test behavior
            if i >= 40:
                break

            agency  = {
                'id': row[ID_ROW],
                'name': row[NAME_ROW],
                'website': row[WEBSITE_ROW]
            }
            agency_instance = ProcessAgencyInfo(agency)
            agency_details = agency_instance.process_agency_info()
            all_agency_info.append(agency_details)
            i+=1
            print(agency)
        all_info_json = json.dumps(all_agency_info)
        print(all_info_json)


fill_agency_objects()