import csv, os
from civic_pulse.models import Agency

ID_ROW = 1
NAME_ROW = 2
PHONE_ROW = 5
BACKUP_PHONE_ROW = 6
WEBSITE_ROW = 8
TWITTER_ROW = 9
BACKUP_TWITTER_ROW = 10
FACEBOOK_ROW = 17


def fill_agency_objects(filepath=os.path.join(os.path.dirname(__file__),
                                              "../data/agencies.csv")):

    with open(filepath) as file:
        reader = csv.reader(file)
        next(reader, None)  # skip the headers

        i = 0
        for row in reader:
            # only run 100 to test behavior
            if i >= 100:
                return

            optional_args = {
                'phone_number': row[PHONE_ROW] if row[PHONE_ROW] else row[BACKUP_PHONE_ROW],
                'website': row[WEBSITE_ROW],
                'twitter': row[TWITTER_ROW] if row[TWITTER_ROW] else row[BACKUP_TWITTER_ROW],
                'facebook': row[FACEBOOK_ROW]
            }

            agency, created = Agency.objects.update_or_create(
                id=row[ID_ROW],
                name=row[NAME_ROW],
                defaults=optional_args
            )
            i+=1
            print(agency)