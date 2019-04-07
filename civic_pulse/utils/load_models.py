import csv, os
from civic_pulse.models import Agency


def fill_agency_objects(filepath=os.path.join(os.path.dirname(__file__),
                                              "../../data/../data/agencies.csv")):
    with open(filepath) as file:
        reader = csv.reader(file)
        next(reader, None)  # skip the headers

        i = 0
        for row in reader:
            try:
                agency, created = Agency.objects.get_or_create(
                    name=row[2]
                )
                print(agency)
                i+=1
            except Exception as e:
                print(e + ": " + agency.__str__())

            if i >= 10:
                return