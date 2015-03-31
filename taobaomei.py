#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import urllib  
import httplib2  
import re
import string, urllib2 

filew1 = open('/Users/yinyue/Desktop/yxlinkpc/新东西/python/taobaomei/aa.txt', 'a')
  
http = httplib2.Http()  
url = 'http://mm.taobao.com/json/request_top_list.htm?type=0&page='

pattern1 = re.compile(r'http://img\d{2}.taobaocdn.com/sns_logo/i\d/[^\s?!_]*')

i = 1
j = 1
while i<=5:
	url1 = url + str(i) 
	i = i + 1
	response, content = http.request(url1)
	lianjie = re.findall(pattern1,content)
	print lianjie
	for lj in lianjie:
		filew1.write(lj+'\n')

filer1 = open('/Users/yinyue/Desktop/yxlinkpc/新东西/python/taobaomei/aa.txt', 'r')
for line in filer1.readlines():
	line = line.strip('\n')
	print line
	response, content = http.request(line)
	taobaomeilj = str(j)+'.jpg'
	j = j + 1
	filew2 = open('image/'+taobaomeilj, 'w')
	filew2.write(content)
	filew2.close()
