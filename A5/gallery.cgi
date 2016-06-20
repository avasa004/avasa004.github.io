#!/usr/bin/python
import os
import Image 
import cgi
import Cookie
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

if handler['role'] == 'Visitor':
	print 'Location: galleryv.cgi'



print "content-type:text/html\n\n"




HTML_Begin = """<!DOCTYPE HTML>
	<html>
	<head>
	<link rel = 'stylesheet' type = 'text/css' href = 'style.css'>
	<title>
	Gallery
	</title>
	</head>
	<body>"""

print HTML_Begin




# names = [os.listdir('pictures') 

# cookies = os.environ['HTTP_COOKIE']
# cookies = cookies.split(';')
# disable = 0
# handler = {}




print "<div class = 'begin'>"
print "<h1>Picture Gallery</h1>"
print "<button onClick = 'reload()' type = 'button'>Refresh</button>"
print "<button id = 'upload' onClick = 'upload()' type = 'button'>Upload New Picture</button>"
print "</div><br/><br/>"

# names = os.listdir('pictures')
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
		print "<form method = 'POST' action = 'edit.cgi' enctype = 'multipart/form-data'>"
		print "<input type = 'hidden' name = 'txt' value =" + txtname + ">"
		print "<input type = 'hidden' name ='title' value = " + title + ">"
		print "<input id = 'edit' type = 'submit' value = 'Edit' name = 'editted'></input>"
		print "</form>"
		print "<form action = 'delete.cgi' method = 'POST' enctype = 'multipart/form-data'>"
		print "<input type = 'hidden' name = 'txt' value =" + txtname + "></input>"
		print "<input type = 'hidden' name ='filename' value = " + name + "></input>"
		print "<input type = 'hidden' name ='title' value = " + title + "></input>"
		print "<input id = 'delete' type = 'submit' value = 'Delete' name = 'deleteit'></input>"
		print "</form>"

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
		
		}


		function disableButtons(){
			if(document.getElementById('edit') != null){
				document.getElementById('edit').disabled = true;
			}

			if(document.getElementById('delete') != null){
				document.getElementById('delete').disabled = true;
			}
			document.getElementById('upload').disabled = true
		}

		function reload(){
			location.reload()
			}

		function upload(){
			window.location ='upload.cgi'
			}
        
        function goToEdit(){
                    window.location = 'edit.cgi';
             }
        
        function onEdit(){
         	document.form1.action = 'edit.cgi';
         	//document.form1.submit();
         	return true;
         }
         function onDelete(){
         	document.form1.action = 'delete.cgi';
         	//document.form1.submit();
         	return true;
         }</script>"""




print '</body></html>'











