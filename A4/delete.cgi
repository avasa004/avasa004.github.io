#!/usr/bin/python

import os
import cgi
import cgitb;cgitb.enable()


form = cgi.FieldStorage()

if('deleted' in form):
	# print "deleting file: " + form['filename'].value
	thumb,ext = os.path.splitext(form['filename'].value)
	thumb = thumb + '_tn.jpg'
	os.remove('pictures/'+form['filename'].value)
	os.remove('pictures/'+form['txt'].value)
	if(os.path.isfile('pictures/'+thumb)):
		os.remove('pictures/'+thumb)
		
	print "location: gallery.cgi"
if('canceled' in form):
	print "location: gallery.cgi"


print "content-type:text/html\n\n"


	



title = form['title'].value

filename = form['filename'].value

txtname = form['txt'].value






print """<!DOCTYPE HTML>
		<html>
		<body>
		<title>
		Delete
		</title>
		</head>
		<body>
		<h1 class = 'header'>Delete Picture</h1>
		<h3>Are you sure you want to delete the picture [""" + title +"""]</h3>
		<form action = 'delete.cgi' method = 'POST'>
		<input type = 'hidden' name = 'title' value = """ + title + """></input>
		<input type = 'hidden' name = 'txt' value =""" + txtname + """></input>
		<input type = 'hidden' name = 'filename' value = """ + filename + """></input>
		<input type = 'submit' value = 'Delete' name = 'deleted'></input>
		<input type = 'submit' value = 'Cancel' name = 'canceled'></input>
		</form>
		</body>
		</html>"""



# if('deleted' in form):
# 	os.remove('pictures/'+form['filename'].value)
# 	os.remove('pictures/'+form['txt'].value)

