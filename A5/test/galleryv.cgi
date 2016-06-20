#!/usr/bin/python


import os
import cgi
import cgitb;cgitb.enable()

handler = {}

cookies = os.environ['HTTP_COOKIE']

cookies = cookies.split(';')

for cookie in cookies:
	cookie = cookie.split('=')
	handler[cookie[0]] = cookie[1]

if 'role' not in handler:
	print 'Location: login.html'

if handler['role'] == 'Owner':
	print 'Location: gallery.cgi'


print 'content-type:text/html\n\n'


HTML_Begin = """<!DOCTYPE HTML>
	<html>
	<head>
	<link rel = 'stylesheet' type = 'text/css' href = 'style.css'>
	<title>
	Gallery
	</title>
	</head>
	<body></body></html>"""

print HTML_Begin

names = os.listdir('pictures')

jpgnames = [name for name in names if name.endswith('jpg')]

for name in jpgnames:
	if(name.endswith('tn.jpg')):
		jpgnames.remove(name)



print "<div class = 'outerDiv' id = 'outerDiv'>"


if(len(jpgnames)):

	for name in jpgnames: 
		basename,ext = os.path.splitext(name)
		txtname = basename +'.txt'
		f = file('pictures/'+txtname,'r')
		title = f.read()
		filepath = 'pictures/'+name
		print "<div name = image class = image id = image><img name = " + title + " src = " + filepath + " onClick = showImage(this)><br/>"
		print "<h3 name = 'title'>" + title + "</h3>"
		print "</div>"

print "</div>"

print """<script>
		var showing = false;
		function showImage(img){
                if(showing == false){
			showing = true;
			var currentDiv = document.getElementById('image')
			newdiv = document.createElement('div')
			var attr = document.createAttribute('class')
			var attr2 = document.createAttribute('onClick')
			var attr3 = document.createAttribute('id')
			attr.value = 'bigdiv'
			attr2.value = 'showImage(this)'
			attr3.value = 'bigdiv'
			newdiv.setAttributeNode(attr)
			//document.insertBefore(newdiv,currentDiv)
			var outerDiv = document.getElementById('outerDiv')
			outerDiv.appendChild(newdiv)
			newdiv.innerHTML = '<img class = ' + 'bigImage' +  ' src = ' + img.src + ' onClick = showImage(this)>'
			newdiv.innerHTML += '<h4 class = ' + 'imageTitle' + '>' + img.name + '</h4>'}
		else{
			showing = false
			newdiv.parentNode.removeChild(newdiv)
		}
		
		}</script>"""


#print '</body></html>'


