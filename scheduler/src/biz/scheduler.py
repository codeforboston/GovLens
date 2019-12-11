from datetime import datetime, timedelta
import os, math, queue, json, asyncio
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from .agency_api_service import AgencyApiService
from .scrape_data import ScraperService


class Scheduler:

    def __init__(self):
        self.queue_size = 0
        self.job_execution_counter = 0
        self.scraper_service = ScraperService()

    def read_settings(self):
        data = {}
        with open(os.path.dirname(os.path.abspath(__file__))+"/job_config.json", 'r') as f:
            data = json.load(f)
        self.agency_list_size = data['agency_batch_size']
        self.job_trigger_settings = data['job_trigger_settings']
        self.interval_between_runs_seconds = data['interval_between_runs_seconds']
        # there is an option to pass all these variables at run time using environment variables
        if os.environ.get('day', None) is not None:
            self.read_settings_from_environment_variables()

    def read_settings_from_environment_variables(self):
        if os.environ.get('agency_batch_size', None) is not None:
            self.agency_list_size = int(os.environ.get('agency_batch_size'))
        else:
            self.agency_list_size = 4
        if os.environ.get('interval_between_runs_seconds', None) is not None:
            self.interval_between_runs_seconds = int(os.environ.get('interval_between_runs_seconds'))
        else:
            self.interval_between_runs_seconds = 20
        if os.environ.get('day', None) is not None:
            print(os.environ.get('day'))
            print(os.environ.get('hour'))
            print(os.environ.get('minute'))
            print(os.environ.get('second'))
            self.job_trigger_settings['day_of_job'] = os.environ.get('day')
        else:
            raise Exception("day of job is not specified in the environment variable")
        if os.environ.get('hour', None) is not None:
            self.job_trigger_settings['hour'] = os.environ.get('hour')
        else:
            raise Exception("hour is not specified in the environment variable")
        if os.environ.get('minute', None) is not None:
            self.job_trigger_settings['minute'] = os.environ.get('minute')
        else:
            raise Exception("minute is not specified in the environment variable")
        if os.environ.get('second', None) is not None:
            self.job_trigger_settings['second'] = os.environ.get('second')
        else:
            raise Exception("second is not specified in the environment variable")

    def scheduled_method(self):
        print(
            f"Started scraping the agency info at {str(datetime.now().strftime('%Y-%m-%d %H:%M:%S'))}")
        agency_api_service = AgencyApiService()
        agency_list = agency_api_service._get()
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
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(self.scraper_service.scrape_data(agencies))
            scheduler = BlockingScheduler()
            scheduler.add_job(self.scrape_scheduled_method,
                              next_run_time=datetime.now()+timedelta(seconds=self.interval_between_runs_seconds))
            scheduler.start()
        else:
            print(
                f"done with scraping at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def reset_schedule_parameters(self):
        self.queue_size = 0
        self.job_queue = None
        print(
            f"Done Scraping the data for the agencies at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    def scrape_websites(self):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.scheduled_method, 'cron',
                          day_of_week=self.job_trigger_settings['day_of_job'], hour=self.job_trigger_settings['hour'], minute=self.job_trigger_settings['minute'], second=self.job_trigger_settings['second'])
        try:
            scheduler.start()
        except (KeyboardInterrupt, SystemExit):
            pass

    def split_data_into_chunks(self, agencies):
        for i in range(0, len(agencies), self.agency_list_size):
            self.job_queue.put(agencies[i:i + self.agency_list_size])
