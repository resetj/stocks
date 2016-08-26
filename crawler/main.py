# -*- coding: utf8 -*-
__author__ = 'cx'

import urllib
import urllib2
import sys 


from settings import *
from utils.checkdata import *

class ThrowOut(Exception):
    def __init__(self, msg):
        self.msg = msg

def main():
    
    print(IsValidTime())
    settingsModule = SettingsClass()

    # url = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C._SZAME&sty=FCOIATA&sortType=C&sortRule=-1&page=1&pageSize=100000&js=var%20quote_123%3d{rank:[(x)],pages:(pc)}&token=7bc05d0d4c3c22ef9fca8c2a912d779c"

    # req = urllib2.Request(url)
    # print req

    # res_data = urllib2.urlopen(req)
    # res = res_data.read()
    #print res



if __name__ == "__main__":
    sys.exit(main())


