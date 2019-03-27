from datetime import datetime, timedelta, date
import requests
import csv
import time
import os
import sys
import databaseoperations


class Scrapper():
    def __init__(self, region):
        super(Scrapper, self).__init__()
        self.region = region
        self.base_headers = ['Position', 'Track Name', 'Artist', 'Streams', 'URL']

    #    def __init__():

    def daterange(self, date1, date2):
        for n in range(int((date2 - date1).days)+1):
            yield date1 + timedelta(n)

    def getDates(self):
        one_day = timedelta(days=1)
        start_dt = date(2019, 3, 3)
        end_dt = datetime.now().date() - (3 * one_day)
        for dt in self.daterange(start_dt, end_dt):
            current_date = dt.strftime("%Y-%m-%d")
            yield current_date
            # all_dates.append(current_date)

    def downloadCSV(self):
        file_counter = 0
        for current_date in self.getDates():
            file_counter += 1
            print("file no. {}".format(file_counter))
            url = "https://spotifycharts.com/regional/us/daily/{}/download".format(current_date)
            time.sleep(0.2)
            with requests.Session() as session:
                download = session.get(url)
                decoded_content = download.content.decode('utf-8')
                cr = csv.reader(decoded_content.splitlines(), delimiter=',')
                next(cr)
                cr.extend([current_date, self.region])
                yield cr

    def insertData(self):
        dump = []
        for file in self.downloadCSV():
            for row in file:
                print('row is {}'.format(row))
            print('type of row is {}'.format(type(row)))

    def createDatabase(self):
        print('yolo')


def main():
    scrapper = Scrapper('us')
    scrapper.createDatabase()
    scrapper.insertData()


if __name__ == '__main__':
    main()
