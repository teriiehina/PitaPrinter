#!/usr/bin/python

import os
import sys
import urllib2
import simplejson

from escpos     import *
from subprocess import call

# filename = "/tmp/git-commiters.txt"
# command  = "git shortlog -sn > " + filename
# sts = os.system(command)

def file_len(fname):
    with open(fname , 'r') as f:
        for i, l in enumerate(f):
            pass
    return i + 1

dn  = os.path.dirname(os.path.realpath(__file__))

# call(["git shortlog -sn > /tmp/git-commiters.txt"])

commiters   = ["aferguen" , "crichard" , "jgodon" ,  "mprot" , "pmeuel" , "vhosune"]
Epson       = printer.Usb(0x04b8,0x0202)
lineWidth   = 42

Epson.set("left", "a", "b", 2, 2)

try:
    for commiter in commiters:
        
        filename = "/tmp/" + commiter + ".txt"
        command  = "git shortlog --branches --no-merges --since yesterday  --author " + commiter + " > " + filename
        print command
        
        os.system(command)
        f  = open("/tmp/" + commiter + ".txt", 'r')
        fn = os.path.join(dn, commiter + ".jpg")
        
        Epson.set("center", "a", "b", 1, 1)
        Epson.image(fn)
        Epson.text("\n\n");
        Epson.set("left", "a", "b", 2, 2)
        
        Epson.text(commiter + "\n")
        
        for line in f:
            Epson.text(line)
            Epson.text("\n")
        
            
        Epson.text("\n")
        Epson.cut()         
        # f.close()
        # fn.close()
            
except Exception:
    print "Unexpected error: " , sys.exc_info()[0]
    Epson.text("Oh no, something wrong happened\n\n")
    Epson.cut()


