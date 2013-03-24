#!/usr/bin/env python
#
# File: hamqthtest.py
#
# Copyright (c) 2013 Steve Conklin
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  
# 02110-1301, USA.
#

from sys import argv
import getpass

from hamqthlib import *

def queryLoginInfo():
    print 'Please provide your login info for the hamqth.com service...'
    username = raw_input('Username: ')
    password = getpass.getpass('Password: ')
    return (username, password)


if len(sys.argv) != 2:
    print "usage:\n\nargv[0] callsign"

qth = QTH(storeCredentials = True, applicationID = 'test')

if not qth.loginInfoExists():
    uname, passw = queryLoginInfo()
    qth.setLoginInfo(username=uname, password=passw, storeCredentials=True)

results = qth.lookupCallsign(argv[1], getBio=True, getActivity=True)
#callsign, getCallsignInfo = True, getBio = False, getActivity = False):
for key in results:
    print "%s : %s" % (key, results[key])

print "done"

