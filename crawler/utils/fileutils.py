# -*- coding: utf-8 -*-
__author__ = 'cx'

import os
import datetime

def CreateFileEnv():
	currentPath = os.getcwd()
	currentPath = os.path.dirname(currentPath)
	# currentPath = os.path.dirname(currentPath)
	currentPath = currentPath + "\\data\\" + datetime.datetime.now().strftime("%Y%m%d")
	if not os.path.exists(currentPath):
		os.makedirs(currentPath)

	return currentPath

def RemoveFile(filename):
	if os.path.isfile(filename):
		os.remove(filename)

def RemoveDir(filedir):
	if os.path.isdir(filedir):
		os.redir(filedir)

def SaveStrToFile(dirpath, filename, str):
	path = dirpath + "\\" + filename
	fp = open(path, 'w')
	fp.write(str)
	fp.close()

# RemoveFile("D:\\GitHub\\stocks\data\\test.txt")
# SaveStrToFile("D:\\GitHub\\stocks\\data", "test.txt", "thiss is a test")