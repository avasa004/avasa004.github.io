#!/usr/bin/python

import os
import Image
import cgi
import cgitb;cgitb.enable()


handler = {}
user = ''
cookies = os.environ['HTTP_COOKIE']
cookies = cookies.split(';')
for cookie in cookies:
	cookie = cookie.split('=')
	handler[cookie[0]] = cookie[1]

if 'role' not in handler:
	print 'Location: login.html'
else:
	if handler['role'] == 'Visitor':
		print 'Location: galleryv.cgi'

form = cgi.FieldStorage()
title = form['title'].value
txtfile = form['txt'].value
if('updated' in form):
	filepath = 'pictures/' + txtfile
	os.remove(filepath)
	fout = file(filepath,'w')
	fout.write(form['title'].value)
	fout.close()
	print "location: gallery.cgi"
if('canceled' in form):
	print "location: gallery.cgi"

print 'content-type:text/html\n\n'


print """<!DOCTYPE HTML>
	<html>
	<head>
	<link rel = 'stylesheet' type = 'text/css' href = 'style.css'>
	<title>
	Edit
	</title>
	</head>
	<body>



<h1 class = 'header'>Enter A New Title</h1>
<form action = 'edit.cgi' method = 'POST' onsubmit = 'return validateForm()'>
<h3 id = error name = 'error'></h3>
Title: <input id = 'title' type = 'text' name = 'title' value = """ + title + """></input>
<input type = 'hidden' name = 'txt' value =""" + txtfile +"""></input>
<input type = 'submit' value = 'Update' name = updated></input>
<input type = 'submit' value = 'Cancel' name = canceled></input>
</form>
</body></html>"""


print """<script>
		function validateForm(){
		  title = document.getElementById('title');
		  if(title.value.length == 0){
		  	document.getElementById('error').innerHTML = "Please Enter A Title";
		  	return false;
		  }
		  return true;
		}</script>"""









