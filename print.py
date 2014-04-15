#!/usr/bin/python

import sys
from escpos import *
""" Seiko Epson Corp. Receipt Printer M129 Definitions (EPSON TM-T88IV) """

Epson = printer.Usb(0x04b8,0x0202)

try:
    
    Epson.set("center", "a", "b", 1, 1)
    Epson.image("jenkins.jpg")

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