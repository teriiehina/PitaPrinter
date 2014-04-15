#!/usr/bin/python

import os
import urllib2
import simplejson
from escpos import *


proxy  = urllib2.ProxyHandler({'http': 'pmeuel:Pitapita1@cerberus.pj.fr:8080'})
req    = urllib2.Request("http://vestale.micro.pj.fr:8765/api/json?pretty=true", None)
opener = urllib2.build_opener(proxy)
res    = opener.open(req)
data   = simplejson.load(res)

jobs_ok = []
jobs_ko = []


for x in data["jobs"]:
    if(x["color"] == "red"):
        jobs_ko.append(x)
    else:
        jobs_ok.append(x)
        

    
Epson = printer.Usb(0x04b8,0x0202)

try:
    
    dn = os.path.dirname(os.path.realpath(__file__))
    fn = os.path.join(dn,"jenkins.jpg")
    
    Epson.set("center", "a", "b", 1, 1)
    Epson.image(fn)

    Epson.set("center", "a", "b", 2, 2)
    Epson.text("\n\nJobs KO\n\n")

    Epson.set("left", "a", "b", 1, 1)
    
    for x in jobs_ko:
        Epson.text(x["name"])
        Epson.text("\n")    
        
    Epson.set("center", "a", "b", 2, 2)
    Epson.text("\n\nJobs OK\n\n")

    Epson.set("left", "a", "b", 1, 1)
    
    for x in jobs_ok:
        Epson.text(x["name"])
        Epson.text("\n")    
    

except Exception:
    Epson.text("Oh no, something wrong happened\n")

Epson.cut()