# -*- coding: utf8 -*-
__author__ = 'cx'

import threading
import time
from settings import *

mutex = threading.Lock()

class ConsumerClass(threading.Thread):
	def __init__(self, t_name, queue):
		threading.Thread.__init__(self, name = t_name)
		self.name = t_name
		self.data = queue

	def run(self):
		# time.sleep(1)
		global mutex
		while True:
			try:
				if mutex.acquire():
					if self.data.empty():
						print "Thread:" + self.name + " done\n"
						mutex.release()
						break
					#do something
					stockId = self.data.get(1)
					print self.name + "\n"

					mutex.release()

			except:
					print "error:" + str(stockId)
