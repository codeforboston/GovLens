from datetime import datetime, timedelta
import os
import math
import queue, json
from apscheduler.schedulers.blocking import BlockingScheduler
from agency_api_service import AgencyApiService
from scrape_data import scrape_data


''' In this module we create a class Sheduler with methods:
 read_settings() - reads job_config.json - parameters for each agency
 scheduled_method() - gets all agencies(AgencyApiService()) and stores them into a list
 scrape_scheduled_method() - schedule method to call scrapers for each agency(from the agencies list) with a timestamp converted to a string
 reset_schedule_parameters() - resets queue_size to 0 and job_queue to None to end when scraping all agencies with a time stamp converted to a string
 scrape_websites() - scrapes each website at a specific time('cron')
 '''
class Scheduler:

    def __init__(self):
        self.queue_size = 0
        self.job_execution_counter = 0
    
    def read_settings(self):
        data = {}
        with open(os.path.dirname(os.path.abspath(__file__))+"/job_config.json", 'r') as f:
            data = json.load(f)
        self.agency_list_size = data['agency_batch_size']
        self.day_of_job = data['day_of_job']
        self.hour = data['hour']
        self.minute = data['minute']
        self.interval_between_runs_seconds = data['interval_between_runs_seconds']

    def scheduled_method(self):
        print(f"Started scraping the agency info at {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}")
        agency_api_service = AgencyApiService()
        agency_list = agency_api_service.get_all_agencies()
        self.queue_size = math.ceil(len(agency_list)/self.agency_list_size)
        self.job_queue = queue.Queue(maxsize=self.queue_size)
        self.split_data_into_chunks(agency_list)
        self.scrape_scheduled_method()

    def scrape_scheduled_method(self):
        self.job_execution_counter = self.job_execution_counter + 1
        print(
            f"Executing the {self.job_execution_counter} job. {self.queue_size - self.job_execution_counter} to be executed at {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}")
        if self.job_queue.empty() is False:
            agencies = self.job_queue.get()
            scrape_data(agencies)
            scheduler = BlockingScheduler()
            scheduler.add_job(self.scrape_scheduled_method,
                              next_run_time=datetime.now()+timedelta(seconds=self.interval_between_runs_seconds))
            scheduler.start()
        else:
            print(f"done with scraping at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def reset_schedule_parameters(self):
        self.queue_size = 0
        self.job_queue = None
        print(f"Done Scraping the data for the agencies at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def scrape_websites(self):
        scheduler = BlockingScheduler()
        scheduler.add_job(self.scheduled_method, 'cron',
                          day_of_week=self.day_of_job, hour=self.hour, minute=self.minute, second=20)
        try:
            scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass
    


    def split_data_into_chunks(self, agencies):
        for i in range(0, len(agencies), self.agency_list_size):
            self.job_queue.put(agencies[i:i + self.agency_list_size])


scheduler_instance = Scheduler()   #Creates a Scheduler instance 
scheduler_instance.read_settings()  #Reads settings for each new istance from job_config.json 
scheduler_instance.scrape_websites() #Scrapes websites for each new object 


