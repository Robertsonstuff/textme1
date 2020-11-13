from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler

from textme1 import send_goodtimes

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(send_goodtimes, 'interval', seconds=15)

sched.start()