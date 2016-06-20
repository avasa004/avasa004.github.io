#!/usr/bin/python

import cgi
import cgitb;cgitb.enable()
import os


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




print '<html><head><link rel="stylesheet" type="text/css" href="styles.css"><title>Owner Page</title></head><body>'

print "<h1 align = 'center'>Owner Page</h1>"


print """<div class = 'OwnerForm'>
		<h2>Add New User:</h2>
		<h4 class = 'error' id = 'error1'></h4 class = 'error'>
		<form action = 'add.cgi' onsubmit = 'return validateForm1();'>
		Username: <input id = 'user1' type = 'text' name = 'user'></input></br>
		Password: <input id = 'pass1' type = 'password' name = 'password'></input></br></br>
		<input type = 'submit' value = 'Add User'></input>
		</form>

		<h2>Delete Account:</h2>
		<h4 class = 'error' id = 'error2'></h4 class = 'error'>
		<form action = 'deleteuser.cgi' onsubmit = 'return validateForm2();'>
		Username: <input id = 'user2' type = 'text' name = 'user'></input></br></br>
		<input type = 'submit' value = 'Delete User'></input>
		</form>

		<h2>Change Password:</h2>
		<h4 class = 'error' id = 'error3'></h4 class = 'error'>
		<form action = 'changepass.cgi' onsubmit = 'return validateForm3();'>
		Username: <input id = 'user3' type = 'text' name ='user'></input></br>
		New password: <input id = 'pass3' type = 'password' name = 'password'></input></br></br>
		<input type = 'submit' value = 'Change Password'></input>
		</form>"""


print """<form action = 'gallery.cgi'>
		<input type = 'submit' value = 'Go To Gallery'></input>
		</form>"""

print """</div>"""

print """<script>
		
		function validateForm1(){

			var user1 = document.getElementById('user1');
			var pass1 = document.getElementById('pass1');

			if(user1.value.length == 0){
				document.getElementById('error1').innerHTML = 'Need Username to create account';
				return false;
			}

			if(pass1.value.length == 0){
				document.getElementById('error1').innerHTML = 'Need Password to create account';
				return false;
			}
			return true;
		}

		function validateForm2(){
			var user2 = document.getElementById('user2');

			if(user2.value.length == 0){
				document.getElementById('error2').innerHTML = 'Need Username to delete account';
				return false;
			}
			return true;
		}


		function validateForm3(){

			var user3 = document.getElementById('user3');
			var pass3 = document.getElementById('pass3');

			if(user3.value.length == 0){
				document.getElementById('error3').innerHTML = 'Need Username to change password';
				return false;
			}

			if(pass3.value.length == 0){
				document.getElementById('error3').innerHTML = 'Need new password to change password'
				return false;
			}
			return true;
		}
		</script>"""

print '</body></html>'