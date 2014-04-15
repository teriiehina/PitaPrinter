#!/usr/bin/python

import os
import sys
import urllib2
import simplejson
from escpos import *

def get_json_at_url(url):
    
    proxy  = urllib2.ProxyHandler({'http': 'pmeuel:Pitapita1@cerberus.pj.fr:8080'})
    req    = urllib2.Request(url, None)
    opener = urllib2.build_opener(proxy)
    res    = opener.open(req)
    data   = simplejson.load(res)
    
    return data


gitlab_host     = "http://lpjfr31.pj.fr/"
private_token   = "YhYNmGhfwwqNCfCioHP3"
pagination      = "&per_page=100"

projects_url    = gitlab_host + "api/v3/projects?private_token=" + private_token + pagination
projects        = get_json_at_url(projects_url)

users_url       = gitlab_host + "api/v3/users?private_token=" + private_token + pagination
users           = get_json_at_url(users_url)

lineWidth   = 42

Epson       = printer.Usb(0x04b8,0x0202)

try:
    Epson.set("center", "a", "normal", 1, 1)
    Epson.image("gitlab.jpg");
    Epson.text("\n\n");
    
    Epson.set("left", "a", "normal", 1, 1)

    for user in users:
        Epson.text(user["name"]);
        Epson.text("\n\n");
    
    

except Exception:
    print "Unexpected error: " , sys.exc_info()[0]
    
    Epson.text("Oh no, something wrong happened\n\n")

# Apparently, this cut() method is also used to close the USB
# connection to the printer
Epson.cut()

