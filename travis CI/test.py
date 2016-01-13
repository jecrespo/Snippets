#!/usr/bin/python
# -*- coding: utf-8 -*-

import urllib2

def gethtml(url):
    try:
       req = urllib2.Request(url)
       return urllib2.urlopen(req).read()
    except:
        time.sleep(2)
        print("Web no accesible")
        return ''

url = 'localhost'
web = gethtml(url)
inicio = web.find("Temperatura")
temperatura=web[22:27]

print(temperatura)