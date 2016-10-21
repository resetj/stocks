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

class ThrowOut(Exception):
    def __init__(self, msg):
        self.msg = msg

def main():

    if IsValidDay():
    # if True:
        starttime = datetime.datetime.now()

        settingsModule = SettingsClass()
        settingsModule.SetDataDir(CreateFileEnv())

        print "urlShangzhengA:%s\n" % settingsModule.urlShangzhengA
        print "urlShenzhengA:%s\n" % settingsModule.urlShenzhengA

        # 下面是获取深证A股的列表
        req = urllib2.Request(settingsModule.urlShangzhengA)
        response = urllib2.urlopen(req)
        responseData = response.read()
        jsonData = re.match(r"(var quote_123=)(.*)", responseData).group(2)
        SaveStrToFile(settingsModule.dataDir, "shangzhengA.txt", jsonData)
        rank = "rank"
        pages = "pages"
        rankList = eval(jsonData).get("rank")

        queueStocks = Queue()
        # queueStocks.put("603777")
        # queueStocks.put("600321")
        for stock in rankList:
            stockList = stock.split(",")
            queueStocks.put(str(stockList[1]))

        thread_list = list()
        maxThreadNum = 200
        for i in range(maxThreadNum):
            consumer = ConsumerClass("Consumer" + str(i), queueStocks, 1)
            consumer.start()
            thread_list.append(consumer)

        for thread in thread_list:
            thread.join()

        print "\nAll ShangzhengA has done!\n"


        # 下面是获取深证A股的列表
        req = urllib2.Request(settingsModule.urlShenzhengA)
        response = urllib2.urlopen(req)
        responseData = response.read()
        jsonData = re.match(r"(var quote_123=)(.*)", responseData).group(2)
        SaveStrToFile(settingsModule.dataDir, "shenzhengA.txt", jsonData)
        rank = "rank"
        pages = "pages"
        rankList = eval(jsonData).get("rank")

        queueStocks = Queue()
        # queueStocks.put("300553")
        for stock in rankList:
            stockList = stock.split(",")
            queueStocks.put(str(stockList[1]))

        thread_list = list()
        maxThreadNum = 200
        for i in range(maxThreadNum):
            consumer = ConsumerClass("Consumer" + str(i), queueStocks, 2)
            consumer.start()
            thread_list.append(consumer)

        for thread in thread_list:
            thread.join()

        print "\nAll ShenzhengA has done!\n"

        endtime = datetime.datetime.now()
        print "time:" + str((endtime - starttime).seconds) + "s."


if __name__ == "__main__":
    sys.exit(main())


