# -*- coding: utf-8 -*-
import sys, urllib, urllib2, json
import datetime

def checkWorkingDay(data):
    #http://apistore.baidu.com.cn/apiworks/servicedetail/1116.html
    url = 'http://apis.baidu.com/xiaogg/holiday/holiday?d=' + str(data)
    req = urllib2.Request(url)
    req.add_header("apikey", "ab5247943dfe888b06872324ce25fa10")
    resp = urllib2.urlopen(req)
    content = resp.read()
    if(content):
        if (int(content) == 0 and\
            datetime.datetime.now().weekday() != 5 and\
            datetime.datetime.now().weekday() != 6):
            return True
        else:
            return False

def checkWorkingTime(time):
    if (("091500" <= time and "113000" >= time) or\
        ("130000" <= time and "150000" >= time)):
        return True
    else:
        return False

def isValidTime():
    return checkWorkingDay(datetime.datetime.now().strftime("%Y%m%d")) and\
           checkWorkingTime(datetime.datetime.now().strftime("%H%M%S"))

print(isValidTime())
#print(checkWorkingDay("20161015"))
#print(checkWorkingTime("091000"))



