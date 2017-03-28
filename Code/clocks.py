# -*- coding: utf-8 -*-
#   !pip install pytz
#   sudo easy_install --upgrade pytz

from datetime import datetime, date, time, tzinfo
from pytz import utc, all_timezones, timezone

TimeFormatLong = "%Y-%m-%d, %H:%M:%S %Z %z"

def Time(TZInfo = timezone('UTC')): return datetime.now(TZInfo)

def TimeZoneList(region = None):
    '''
    Provides information for querying http://www.iana.org/time-zones
    '''
    if region != None:
        return [zone for zone in all_timezones if region in zone]
    else:
        return len(TimeZoneList(''))

class Clock(object):
    '''
    Clock objects simplifying date, time and timezone operations
    '''
    def __init__(self, city, zoneTag):
        self.TZCity = city
        self.TZObject = timezone(zoneTag)
        self.TZMoniker = self.localTime().strftime("%Z")
    def __str__(self):
        return (self.localTime().strftime(TimeFormatLong) + " " + str(self.localTime().dst()))
    def city(self): return self.TZCity
    def moniker(self): return self.TZMoniker
    def timezone(self): return self.TZObject
    def localTime(self): return datetime.now(self.timezone())
    def offset(self): return self.TZObject.utcoffset(datetime.now())
    def isDST(self): return bool(self.localTime().dst())

def Clocks():
    return {'Zulu':Clock('Zulu', 'UTC'),
            'GMT':Clock('Greenwich', 'GMT'),
            'CET':Clock('CET', 'Europe/Brussels'),
            'London':Clock('London', 'Europe/London'),
            'Frankfurt':Clock('Frankfurt', 'Europe/Berlin'),
            'Paris':Clock('Paris', 'Europe/Paris')}

print(Clocks()['London'].localTime().strftime(TimeFormatLong))

'''
CST = timezone("CST6CDT")
print(str(CST))

print('\n')
print(time())
print('\n')
print(Osaka == Tokyo)
print(Paris == Frankfurt)

London.timezone()
print('...')
print(bool(Tokyo.localTime().dst()))
print(str(London))
print(London.city())
print(London.moniker())
print(London.localTime().strftime(TimeFormatLong))
print(London.offset())
'''

Zulu = Clock('Zulu', 'UTC')
London = Clock('London', 'Europe/London')
New_York = Clock('New York', 'US/Eastern')
Chicago = Clock('Chicago', 'US/Central')
Montreal = New_York
Winnipeg = Chicago

Tokyo = Clock('Tokyo', 'Asia/Tokyo')
Osaka = Tokyo
Seoul = Clock('Seoul', 'Asia/Seoul')
Busan = Seoul

Singapore = Clock('Singapore', 'Asia/Singapore')
Hong_Kong = Clock('Hong Kong', 'Asia/Hong_Kong')
Shanghai = Clock('Shanghai',  'Asia/Shanghai')
Dalian = Shanghai

Sydney = Clock('Sydney', 'Australia/Sydney')

Frankfurt = Clock('Frankfurt', 'Europe/Berlin')
Paris = Clock('Paris', 'Europe/Paris')
Madrid = Clock('Madrid', 'Europe/Madrid')
Milan = Clock('Milan', 'Europe/Rome')
Stockholm = Clock('Stockholm', 'Europe/Stockholm')
Zurich = Clock('Zurich', 'Europe/Zurich')

print(Zurich.localTime().strftime(TimeFormatLong))
