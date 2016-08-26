# -*- coding: utf8 -*-
__author__ = 'cx'

class SettingsClass:
    
    token = "7bc05d0d4c3c22ef9fca8c2a912d779c"
    shangzhengA = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C.2&sty=FCOIATA&sortType=C&sortRule=-1&page=1&pageSize=100000&js=var%%20quote_123%%3d{rank:[(x)],pages:(pc)}&token=%s"
    hushengA = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C._SZAME&sty=FCOIATA&sortType=C&sortRule=-1&page=1&pageSize=100000&js=var%%20quote_123%%3d{rank:[(x)],pages:(pc)}&token=%s"
    singleTransaction = "http://hqdigi2.eastmoney.com/EM_Quote2010NumericApplication/CompatiblePage.aspx?Type=OB&stk=%d&Reference=xml&limit=0&page=%d"
    
    def __init__(self):
        self.url = "test"

