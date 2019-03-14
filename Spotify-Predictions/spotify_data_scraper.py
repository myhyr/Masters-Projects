import pandas as py
from bs4 import BeautifulSoup as bs
from datetime import datetime,timedelta,date
import re
import requests
import os
import time
import csv

def daterange(date1, date2):
    for n in range(int ((date2 - date1).days)+1):
        yield date1 + timedelta(n)

one_day = timedelta(days=1)
start_dt = date(2017, 1, 1)
end_dt = datetime.now().date() - (3 * one_day)
all_dates = []
for dt in daterange(start_dt, end_dt):
    current_date = dt.strftime("%Y-%m-%d")
    url = "https://spotifycharts.com/regional/us/daily/%s/download" % (current_date)
    all_dates.append(current_date)



with requests.Session() as session:
    download = session.get(url)

    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    next(cr)
    my_list = list(cr)
    firstline = True
    i = 0
    for row in my_list:

        if firstline or row[0] == 'Position':
            firstline= False
            continue
        print(i+1)
        i += 1
        print(row)

# def connectSpotify():
    # for i in range(5): # try 5 times
    #     try:
    #         #use the browser to access the url
    #         response=requests.get(url,headers = { 'User-Agent':'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36', })
    #         success=True # success
    #         break # we got the file, break the loop
    #     except:# browser.open() threw an exception, the attempt to get the response failed
    #         print ('failed attempt',i)
    #
    # # all five attempts failed, return  None
    # if not success: return None
