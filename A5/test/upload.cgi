#!/usr/bin/python

import os
import Image
import cgi

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

print 'content-type:text/html\n\n'

print """<!DOCTYPE HTML>
	<html>
	<head>
	<link rel = 'stylesheet' type = 'text/css' href = 'style.css'>
	<title>
	Upload
	</title>
	</head>
	<body>



<h1 class = 'header'>Upload A New JPEG Picture</h1>


 <div class = 'upload'>
 <form action = 'upload.cgi' method = 'POST' onsubmit = 'return validateForm()' enctype = 'multipart/form-data'>
 <h2 id = error></h2>
 Title: 
 <input name = 'title' type = 'text' id ='text'></input></br></br></br>
 File: <input  name = 'file' type = 'file' id = 'file'></input></br></br></br>
 <input type = 'submit' value = 'upload' name = 'uploaded'></input>
 <button type = 'button' onClick = 'goToGallery()'>Cancel</button>
 </form>
 </div>

<script>
		function validateForm(){
			var text = document.getElementById('text');
			var file = document.getElementById('file');
			if(text.value.length == 0){
				document.getElementById('error').innerHTML = 'Please Enter A title';
				return false;
			}
			if(file.value.length == 0){
				document.getElementById('error').innerHTML = 'Please Choose a File';
				return false;
			}

			var filename = file.value;
			ext = filename.split('.').pop();
			if(ext!='jpg')
				{
					document.getElementById('error').innerHTML = 'Plesae choose an image(jpg) file';
					return false
				}
			document.getElementById('error').innerHTML = '';
			return true;
		}

		function goToGallery(){
			window.location = 'gallery.cgi'
		}
		</script>

</body></html>"""


form = cgi.FieldStorage()

# upload = true

if('uploaded' in form):
		
	if not os.path.isdir('pictures'):
		os.mkdir('pictures',0755)
	fileitem = form['file']
	print "Name of file: " + fileitem.filename

	fout = file(os.path.join('pictures',fileitem.filename),'w')
	while 1:
		chunk = fileitem.file.read(100000)
		if not chunk: break
		fout.write(chunk)
	fout.close()
	print "File Was written successfully"

	name,ext = os.path.splitext(fileitem.filename)
	name = name + '.txt'
	fout = file(os.path.join('pictures',name),'w')
	fout.write(form['title'].value)
	fout.close()

	thumb,ext = os.path.splitext(fileitem.filename)
	thumb = thumb + '_tn.jpg'

	size = (140,140)
	filepath = os.path.join('pictures',fileitem.filename)
	
	im=Image.open(os.path.join('pictures',fileitem.filename))

	im.thumbnail(size)
	im.save(os.path.join('pictures',thumb), 'JPEG')





	# if not fileitem.file: 
	# 	print 'Nothing in File'
	# 	return
	# #fout = file(os.path.join('pictures',fileitem.filename),'w')

	# print 'File written successfully'



