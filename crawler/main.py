# -*- coding: utf8 -*-
__author__ = 'cx'

import urllib
import urllib2
import sys
import datetime
from Queue import Queue


from settings import *
from threads import *

from utils.checkdate import *
from utils.fileutils import *
from utils.match import *

class ThrowOut(Exception):
    def __init__(self, msg):
        self.msg = msg

def main():

    if IsValidDay():

        settingsModule = SettingsClass()
        settingsModule.SetDataDir(CreateFileEnv())
        # 下面是获取上证A股的列表
        print "url:%s\n" % settingsModule.urlShangzhengA
        req = urllib2.Request(settingsModule.urlShangzhengA)
        response = urllib2.urlopen(req)
        responseData = response.read()
        jsonData = MatchList(responseData)
        SaveStrToFile(settingsModule.dataDir, "shangzhengA.txt", jsonData)
        rank = "rank"
        pages = "pages"
        rankList = eval(jsonData).get("rank")

        queueStocks = Queue()
        for stock in rankList:
            stockList = stock.split(",")
            queueStocks.put(int(stockList[1]))

        thread_list = list()
        maxThreadNum = 100
        for i in range(maxThreadNum):
            consumer = ConsumerClass("Consumer" + str(i), queueStocks)
            consumer.start()
            thread_list.append(consumer)

        for thread in thread_list:
            thread.join()

        print "All has done!\n"


        # 下面是获取沪深A股的列表



if __name__ == "__main__":
    sys.exit(main())


