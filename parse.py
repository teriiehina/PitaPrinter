#!/usr/bin/python

import urllib2
import simplejson

proxy  = urllib2.ProxyHandler({'http': 'pmeuel:Pitapita1@cerberus.pj.fr:8080'})

# req    = urllib2.Request("http://vimeo.com/api/v2/video/38356.json", None)
req    = urllib2.Request("http://vestale.micro.pj.fr:8765/api/json?pretty=true", None)

opener = urllib2.build_opener(proxy)

f    = opener.open(req)
data = simplejson.load(f)

# print data["jobs"]

jobs_ok = []
jobs_ko = []


for x in data["jobs"]:
    if(x["color"] == "red"):
        jobs_ko.append(x)
    else:
        jobs_ok.append(x)

print "jobs ko"

for x in jobs_ko:
    print x

print "jobs ok"

for x in jobs_ok:
    print x

