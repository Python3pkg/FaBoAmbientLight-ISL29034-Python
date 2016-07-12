# coding: utf-8
## @package FaBoRTC_PCF2129
#  This is a library for the FaBo Ambient Light I2C Brick.
#
#  http://fabo.io/217.html
#
#  Released under APACHE LICENSE, VERSION 2.0
#
#  http://www.apache.org/licenses/
#
#  FaBo <info@fabo.io>

import FaBoAmbientLight_ISL29034
import time
import sys

light = FaBoAmbientLight_ISL29034.ISL29034()

try:
    while True:

        lux  = light.read()

        print "Lux = ", lux
        time.sleep(0.5)

except KeyboardInterrupt:
    sys.exit()
