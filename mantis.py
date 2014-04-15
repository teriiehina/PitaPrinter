#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import uuid
import suds
import urllib2
import logging

from suds   import bindings
from escpos import *
from SOAPpy import SOAPProxy

from email.mime.multipart import MIMEMultipart

t           = suds.transport.http.HttpTransport()
proxy       = urllib2.ProxyHandler({'https': 'pmeuel:Pitapita1@cerberus.pj.fr:8080'})
opener      = urllib2.build_opener(proxy)
t.urlopener = opener

client = suds.client.Client('https://dsem.pagesjaunes.fr/mantis/api/soap/mantisconnect.php?wsdl' , transport=t)
get = client.service.mc_issue_get('pmeuel','pitapita',sys.argv[1])



Epson = printer.Usb(0x04b8,0x0202)

try:
    
    dn = os.path.dirname(os.path.realpath(__file__))
    fn = os.path.join(dn,"mantis.jpg")
    
    Epson.set("center", "a", "b", 1, 1)
    Epson.image(fn)

    Epson.set("center", "a", "b", 2, 2)
    
    Epson.text(get.project.name.encode("utf-8"))
    Epson.text("\n\n")
    
    Epson.set("left", "a", "b", 2, 2)
    
    Epson.text(get.summary.encode("utf-8"))
    Epson.text("\n\n")
    
    Epson.set("left", "a", "b", 1, 1)
    
    Epson.text(get.description.encode("utf-8"))
    Epson.text("\n\n")
    
    Epson.set("left", "a", "U", 1, 1)
    Epson.text("Soumis par: ")
    Epson.text(get.reporter.real_name.encode("utf-8"))
    Epson.text("\n")
    Epson.text("le: ")
    Epson.text(get.date_submitted.ctime())
    Epson.text("\n")
    Epson.text("MAJ: ")
    Epson.text(get.last_updated.ctime())

    # Epson.set("center", "a", "b", 1, 1)
    # Epson.text("un titre comme un autre\n")
    # 
    # Epson.set("center", "a", "normal", 1, 1)
    # Epson.text("\n\n");
    # Epson.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ornare nibh sed dignissim lacinia. Fusce semper eros at augue suscipit interdum. Curabitur non lacus cursus, dapibus arcu ac, tristique elit.\n")

    # type can be "B" "U" "U2" "BU" "BU2" "NORMAL"
#    Epson.cut("part")

#    Epson.set("left", "b", "normal", 1, 1)
#    Epson.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ornare nibh sed dignissim lacinia. Fusce semper eros at augue suscipit interdum. Curabitur non lacus cursus, dapibus arcu ac, tristique elit.\n")

    # Epson.set("font" , "B")
    # Epson.text("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed ornare nibh sed dignissim lacinia. Fusce semper eros at augue suscipit interdum. Curabitur non lacus cursus, dapibus arcu ac, tristique elit.\n")

    # Print QR Code
    # Epson.qr("You can readme from your smartphone")
    # Print barcode
    # Epson.barcode('1324354657687','EAN13',64,2,'','')
    

except Exception:
    Epson.text("Oh no, something wrong happened\n")
    print "Unexpected error:", sys.exc_info()[0]

# Apparently, this cut() method is also used to close the USB
# connection to the printer
Epson.cut()

# for x in get:
#     print x
    # sr.Title.encode("utf-8")