#!/usr/bin/python

import plistlib
import sys

try:
	plist = plistlib.Plist.fromFile('/Library/Preferences/DirectoryService/ActiveDirectory.plist')

	for key in plist['AD Domain Node List']:

		plist['AD Domain Node List'][key]['LDAP Connection Timeout'] = " & timeOutValue & "
		plist['LDAP Connection Timeout'] = " & timeOutValue & "

		plist.write('/Library/Preferences/DirectoryService/ActiveDirectory.plist')

except IOError, (strerror):
	print strerror

except:
	print 'Unexpected error:', sys.exc_info()[0]
