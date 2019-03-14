import pandas as py
from bs4 import BeautifulSoup as bs
from datetime import datetime, timedelta, date
import re
import requests
import os
import time
import csv


class Scrapper():
    def daterange(self, date1, date2):
        for n in range(int((date2 - date1).days)+1):
            yield date1 + timedelta(n)

    def getDates(self):
        one_day = timedelta(days=1)
        start_dt = date(2017, 1, 1)
        end_dt = datetime.now().date() - (3 * one_day)
        for dt in self.daterange(start_dt, end_dt):
            current_date = dt.strftime("%Y-%m-%d")
            yield current_date
            # all_dates.append(current_date)

    def downloadCSV(self):
        for current_date in self.getDates():
            url = "https://spotifycharts.com/regional/us/daily/%s/download" % (current_date)
            with requests.Session() as session:
                download = session.get(url)
                decoded_content = download.content.decode('utf-8')
                cr = csv.reader(decoded_content.splitlines(), delimiter=',')
                next(cr)

def main():
    scrapper = Scrapper()
    scrapper.downloadCSV()


if __name__ == '__main__':
    main()
