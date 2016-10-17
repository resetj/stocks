# -*- coding: utf8 -*-
__author__ = 'cx'

import re

def MatchList(rawstring):
	return re.match(r"(var quote_123=)(.*)", rawstring).group(2)


