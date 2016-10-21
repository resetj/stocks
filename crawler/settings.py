# -*- coding: utf8 -*-
__author__ = 'cx'

import re

class Singleton(object):  
	def __new__(cls, *args, **kw):  
		if not hasattr(cls, '_instance'):  
			orig = super(Singleton, cls)  
			cls._instance = orig.__new__(cls, *args, **kw)  
		return cls._instance 

class SettingsClass(Singleton):

	token = "7bc05d0d4c3c22ef9fca8c2a912d779c"
	shangzhengA = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C.2&sty=FCOIATA&sortType=C&sortRule=-1&page=1&pageSize=100000&js=var%%20quote_123%%3d{rank:[(x)],pages:(pc)}&token=%s"
	shenzhengA = "http://nufm.dfcfw.com/EM_Finance2014NumericApplication/JS.aspx?type=CT&cmd=C._SZAME&sty=FCOIATA&sortType=C&sortRule=-1&page=1&pageSize=100000&js=var%%20quote_123%%3d{rank:[(x)],pages:(pc)}&token=%s"
	
	urlSingleTransaction = "http://hqdigi2.eastmoney.com/EM_Quote2010NumericApplication/CompatiblePage.aspx?Type=OB&stk=%s&Reference=xml&limit=0&page="

	# http://hqdigi2.eastmoney.com/EM_Quote2010NumericApplication/CompatiblePage.aspx?Type=OB&stk=601002&Reference=xml&limit=0&page=1
	# http://hqdigi2.eastmoney.com/EM_Quote2010NumericApplication/CompatiblePage.aspx?Type=OB&stk=6010021&Reference=xml&limit=0&page=1&rt=0.49412034248566217

	def __new__(cls, *args, **kw):
		if not hasattr(cls, '_instance'):
			orig = super(Singleton, cls)
			cls._instance = orig.__new__(cls, *args, **kw)
		return cls._instance

	def __init__(self):
		self.urlShangzhengA = self.shangzhengA % self.token
		self.urlShenzhengA = self.shenzhengA % self.token

	def SetDataDir(self,dir):
		self.dataDir = dir

	def GetUrlSingleTransaction(self, id):
		pattern = re.compile(r'6')
		if pattern.match(id):
			return self.urlSingleTransaction % (id + "1")
		else:
			return self.urlSingleTransaction % (id + "2")
