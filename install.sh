#!/bin/sh

brew install libusb

# Mac OSX Mavericks and Xcode 5.1 give a cumbersome error 
# if we don't install pil using the two following tricks
ln -s /usr/local/include/freetype2 /usr/local/include/freetype
sudo ARCHFLAGS="-Wno-error=unused-command-line-argument-hard-error-in-future" easy_install pil

sudo easy_install pyusb
sudo easy_install suds
sudo easy_install qrcode
sudo easy_install pyserial
sudo easy_install SOAPpy

wget http://python-escpos.googlecode.com/files/python-escpos-1.0-1.zip
unzip python-escpos-1.0-1.zip

cd python-escpos-1.0-1
python setup.py build
sudo python setup.py install

cd ..
rm python-escpos-1.0-1.zip
rm -Rf python-escpos-1.0-1

