# -*- coding: utf8 -*-
__author__ = 'cx'

import threading
import time
import urllib
import urllib2
import sys
import datetime
import re
# import signal

from settings import *
from utils.fileutils import *

mutex = threading.Lock()
settingsClass = SettingsClass()

# def handler(signum, frame):
# 	raise AssertionError

class ConsumerClass(threading.Thread):

	def __init__(self, name, queue, type):
		threading.Thread.__init__(self, name = name)
		self.name = name
		self.queue = queue
		self.type = type

	def run(self):
		# time.sleep(1)
		global mutex
		while True:
			try:
				if mutex.acquire():
					if self.queue.empty():
						# print "Thread:" + self.name + " done\n"
						mutex.release()
						break

					# signal.signal(signal.SIGALRM, handler)
					# signal.alarm(5)

					self.stockId = self.queue.get(1)
					# print self.name + "\n"

					url = settingsClass.GetUrlSingleTransaction(self.stockId)
					req = urllib2.Request(url + "1")
					response = urllib2.urlopen(req)
					responseData = response.read()
					datas = re.match(r"(var jsTimeSharingData=)(.*)(;)", responseData).group(2)
					
					pages = "pages"
					data = "data"
					dic_data = eval(datas)
					pages_num = dic_data.get("pages")

					dic_alldata = {"data" : []}
					
					if pages_num != 0:
						for i in range(pages_num):
							# url_tmp = urllib2.urlopen(url+str(i+1))
							url_tmp = url + str(i + 1)
							req = urllib2.Request(url_tmp)
							response = urllib2.urlopen(req)
							responseData = response.read()
							datas = re.match(r"(var jsTimeSharingData=)(.*)(;)", responseData).group(2)
							dic_data = eval(datas)
							data_page = dic_data.get("data")
							for item in data_page:
								dic_alldata["data"].append(item)
					if 1 == self.type:
						SaveStrToFile(settingsClass.dataDir, "shangzhengA_" + self.stockId + ".txt", str(dic_alldata))
					else:
						SaveStrToFile(settingsClass.dataDir, "shenzhengA_" + self.stockId + ".txt", str(dic_alldata))
					
					# signal.alarm(0)
					print self.stockId
					mutex.release()
			except e:
				print e + ":" + self.stockId
				mutex.release()



