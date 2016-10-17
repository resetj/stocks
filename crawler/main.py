# -*- coding: utf8 -*-
__author__ = 'cx'

import urllib
import urllib2
import sys
import datetime


from settings import *

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
        req = urllib2.Request(settingsModule.urlShangzhengA)
        response = urllib2.urlopen(req)
        responseData = response.read()
        jsonData = MatchList(responseData)
        SaveStrToFile(settingsModule.dataDir, "shangzhengA.txt", jsonData)
        rank = "rank"
        pages = "pages"
        rankList = eval(jsonData).get("rank")

        print rankList[1]




        # 下面是获取沪深A股的列表



if __name__ == "__main__":
    sys.exit(main())


