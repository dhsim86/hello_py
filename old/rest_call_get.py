#!/usr/bin/env python

# Check environment
import sys
import datetime
import pytz
import pip

def try_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', '--user', package])

try_install('requests')
import requests

try_install('json')
import json

class GetMeterParam():
    def __init__(self, year, month, date, hour, meter_type, app_key):
        self.year = year
        self.month = month
        self.date = date
        self.hour = hour
        self.meter_type = meter_type
        self.app_key = app_key

    def get_time(self):
        timezone = pytz.timezone("Asia/Tokyo")
        dt = datetime.datetime(int(self.year), int(self.month), int(self.date), int(self.hour), 0, 0, 0, timezone)
        return dt.isoformat()

param = GetMeterParam(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])
url = 'http://alpha-meter-image.kr.cloud.toastoven.net:10082/metering/v2.5/meters'

query_param = {
    'startTime': param.get_time(),
    'endTime': param.get_time(),
    'type': param.meter_type,
    'appKey': param.app_key
}

r = requests.get(url, params=query_param)
# print(r.text)

jsonString = r.text
response = json.loads(jsonString)
# print(response['meterBeanList'][0]['amount'])

