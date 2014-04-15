#!/usr/bin/python

import sys
from escpos import *
""" Seiko Epson Corp. Receipt Printer M129 Definitions (EPSON TM-T88IV) """

Epson = printer.Usb(0x04b8,0x0202)

try:
    
    Epson.set("center", "a", "b", 1, 1)
    Epson.image("sudoku.jpg")

except Exception:
    Epson.text("Oh no, something wrong happened\n")
    print "Unexpected error:", sys.exc_info()[0]

# Apparently, this cut() method is also used to close the USB
# connection to the printer
Epson.cut()