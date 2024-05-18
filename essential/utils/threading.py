# myapp/threading.py

import threading
import time
from datetime import datetime, timedelta

class PeriodicTask(threading.Thread):
    def __init__(self, interval, task, *args, **kwargs):
        threading.Thread.__init__(self)
        self.interval = interval
        self.task = task
        self.args = args
        self.kwargs = kwargs
        self.daemon = True  # Daemonize thread
        self.stop_event = threading.Event()

    def run(self):
        while not self.stop_event.is_set():
            next_run = datetime.now() + timedelta(seconds=self.interval)
            self.task(*self.args, **self.kwargs)
            sleep_time = (next_run - datetime.now()).total_seconds()
            if sleep_time > 0:
                time.sleep(sleep_time)
            print("asdas")

    def stop(self):
        self.stop_event.set()
