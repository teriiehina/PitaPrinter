#!/usr/bin/python

import sys
from escpos import *
""" Seiko Epson Corp. Receipt Printer M129 Definitions (EPSON TM-T88IV) """

Epson = printer.Usb(0x04b8,0x0202)
lineWidth = 42

try:
    
    usReference  = "FD - 01 - 01"
    usTitle      = "Developement de la FD"
    usEstimation = "6"
    
    spaceCount  = lineWidth - len(usReference) - len(usEstimation)
    firstLine   = usReference + spaceCount * " " + usEstimation

    Epson.set("left", "a", "u", 2, 2)
    Epson.text(firstLine)
    Epson.text(lineWidth * "-")
    
    
    Epson.set("left", "a", "b", 1, 1)
    Epson.text("\n")
    Epson.text(usTitle)
    Epson.text("\n")
    Epson.text(lineWidth * "-")
    
    Epson.set("left", "a", "b", 2, 2)
    Epson.text("O  -  Stats\n\n")
    Epson.text("O  -  Prod. graphique\n\n")
    Epson.text("O  -  Dev\n\n")
    Epson.text("O  -  Relu\n\n")
    
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
    print "Unexpected error: " , sys.exc_info()[0]
    
    Epson.text("Oh no, something wrong happened\n\n")

# Apparently, this cut() method is also used to close the USB
# connection to the printer
Epson.cut()