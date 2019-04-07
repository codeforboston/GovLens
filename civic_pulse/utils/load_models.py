import csv, os, json
from civic_pulse.models import Agency, Entry

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

        for row in reader:
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

            print(agency)


def fill_entry_objects(filepath=os.path.join(os.path.dirname(__file__),
                                              "../../scrapers/sample_data.json")):

    with open(filepath) as file:
        data = json.load(file)

        for entry in data:
            profile = entry['profile']
            update_args = {
                'https_enabled': profile['security_and_privacy']['https']['met_criteria'],
                'has_privacy_policy': profile['security_and_privacy']['privacy_policies']['met_criteria'],
                'mobile_friendly': profile['website_accessibility']['mobile_friendly']['met_criteria'],
                'good_performance': profile['website_accessibility']['performance']['met_criteria'],
                'has_social_media': profile['outreach_and_communication']['social_media_access']['met_criteria'],
                'has_contact_info': profile['outreach_and_communication']['contact_access']['met_criteria'],
            }
            entry, created = Entry.objects.update_or_create(
                id=entry['id'],
                defaults=update_args
            )
            print(entry)