#!/usr/bin/python

import cgi
import cgitb;cgitb.enable()
import os

print 'content-type:text/html\n\n'

if 'HTTP_COOKIE' in os.environ:
	cookies = os.environ['HTTP_COOKIE']
	print cookies
else:
	print 'no'

print 'Hello Visitor'