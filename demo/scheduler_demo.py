from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler


def print_time_job():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


now = datetime.now()
scheduler = BlockingScheduler()
# 周一到周五每天的6点30分调用一次
scheduler.add_job(print_time_job, "cron", day_of_week="1-5", hour=6, minute=30)
# 每个三秒调用一次
scheduler.add_job(print_time_job, "interval", seconds=3)
# 指定执行日期
scheduler.add_job(print_time_job, "date", next_run_time=now.replace(second=(now.second + 5)))

scheduler.start()
