# -*- coding: utf8 -*-
__author__ = 'cx'

import urllib
import urllib2
import sys 


from settings import *
from match import *
from utils.checkdata import *
from utils.fileutils import *

class ThrowOut(Exception):
    def __init__(self, msg):
        self.msg = msg

def main():

    print(IsValidTime())
    settingsModule = SettingsClass()
    print settingsModule.urlShangzhengA

    # url = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C._SZAME&sty=FCOIATA&sortType=C&sortRule=-1&page=1&pageSize=100000&js=var%20quote_123%3d{rank:[(x)],pages:(pc)}&token=7bc05d0d4c3c22ef9fca8c2a912d779c"
    # req = urllib2.Request(url)
    # response = urllib2.urlopen(req)
    # responseData = response.read()
    # print responseData



if __name__ == "__main__":
    sys.exit(main())


