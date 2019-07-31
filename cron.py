# -*- coding: utf-8 -*-
from crontab import CronTab
from datetime import date, timedelta


class CrontabControl:
    def __init__(self):
        self.cron = CronTab()
        self.job = None
        self.all_job = None

    def write_job(self, command, schedule, file_name):
        self.job = self.cron.new(command=command)
        self.job.setall(schedule)
        self.cron.write(file_name)

    def read_jobs(self, file_name):
        self.all_job = CronTab(tabfile=file_name)

    def monitor_start(self, file):
        self.read_jobs(file)
        for _ in self.all_job.run_scheduler():
            print('予定していたスケジュールを実行しました。')


def main():
    words = ['フランス', 'ドイツ']
    tomorrow = (date.today() + timedelta(days=1)).strftime('%Y%m%d')
    schedule = '0 18 * * *'
    file = 'output.tab'

    c = CrontabControl()

    for word in words:
        command = 'python ./slack_post.py' + ' -w ' + word + ' -d ' + tomorrow
        c.write_job(command, schedule, file)

    c.monitor_start(file)


if __name__ == '__main__':
    main()
