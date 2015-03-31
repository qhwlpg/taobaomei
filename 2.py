#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import urllib  
import httplib2  
import re
import string, urllib2 

filew1 = open('/Users/yinyue/Desktop/yxlinkpc/新东西/python/taobaomei/bb.txt', 'a')
  
http = httplib2.Http()  
url = 'http://izhaofuli.com/'

pattern1 = re.compile(r'http://izhaofuli.com/wp-content/uploads/\d{4}/\d{2}/\w*.jpg')
pattern2 = re.compile(r'http://izhaofuli.com/\d*.html/\d*')

i = 1
j = 1
while i<=20:
	url1 = url + str(i) + '.html'  
	i = i + 1
	print 'url1-------->' + url1
	response1, content1 = http.request(url1)
	lianjie1 = re.findall(pattern1,content1)
	#print lianjie1
	for lj1 in lianjie1:
		filew1.write(lj1+'\n')
	url2 = re.findall(pattern2,content1)
	#print 'url2-------->' + url2
	zz = 0
	for yy in url2:
		print 'yy' + str(zz) + yy
		zz = zz + 1
	if url2:
		for u2 in url2:
			response2, content2 = http.request(u2)
			lianjie2 = re.findall(pattern1,content1)
			print lianjie2
			for lj2 in lianjie2:
				filew1.write(lj2+'\n')


filer1 = open('/Users/yinyue/Desktop/yxlinkpc/新东西/python/taobaomei/bb.txt', 'r')
for line in filer1.readlines():
	line = line.strip('\n')
	print line
	response, content = http.request(line)
	taobaomeilj = str(j)+'.jpg'
	j = j + 1
	filew2 = open('image/'+taobaomeilj, 'w')
	filew2.write(content)
	filew2.close()
