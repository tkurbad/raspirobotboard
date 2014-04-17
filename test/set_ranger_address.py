#!/usr/bin/python2

#
# Set a SRF02 ultrasonic ranger to a new address
#

import sys
from torbot.Ranger import Ranger

if len(sys.argv) != 3:
    print "Usage: %s <current address> <new address>" % sys.argv[0]
    sys.exit(1)

ranger = Ranger(int(sys.argv[1]))

print ranger.set_address(int(sys.argv[2]))
