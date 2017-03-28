# -*- coding: utf-8 -*-
#   import datetime
#   !pip install pytz
#   sudo easy_install --upgrade pytz

from datetime import datetime, date, time, tzinfo
from pytz import all_timezones, timezone # as TimeZone

def TimeZoneList(region = None):
    if region != None:
        return [zone for zone in all_timezones if region in zone]
    else: return len(all_timezones)

print(time())

TZ_London = timezone('Europe/London')
TZ_NewYork = timezone('US/Eastern')
TZ_Sydney = timezone('Australia/Sydney')

print TZ_London.utcoffset(datetime.now())
print TZ_NewYork.utcoffset(datetime.now())
print TZ_Sydney.utcoffset(datetime.now())

print(TimeZoneList(''))
