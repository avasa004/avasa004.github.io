#!/usr/bin/python

import cgi
import cgitb;cgitb.enable()
import MySQLdb
import os
import Cookie



#print 'Authenticating...Please Wait. You should be automatically redirected to a new page...'



form = cgi.FieldStorage();

user = form['username'].value

password = form['password'].value

file = open('config','r')

contents = file.read()

contents = contents.split('\n')

uid = contents[1]

uid = uid.split(':')

uid = uid[1]

uid = uid.strip()

dbpassword = contents[2]

dbpassword = dbpassword.split(':')

dbpassword = dbpassword[1]

dbpassword = dbpassword.strip()

timeout = contents[3]

timeout = timeout.split(':')

timeout = timeout[1]

timeout = int(timeout.strip())

file.close()



query = 'select Role,Password from Users where Name = ' + "'" + user + "'"


db = MySQLdb.connect(host='egon.cs.umn.edu', user=uid, passwd=dbpassword, port=3307)

db.select_db(uid)

cursor = db.cursor()

rows_count = cursor.execute(query)

if(rows_count >0):

	for row in cursor:
		if(row[1]==password):
			if(row[0] == 'Owner'):
				
				cookie = Cookie.SimpleCookie()

				cookie['user'] = user
				cookie['role'] = 'Owner'

				cookie['user']['max-age'] = timeout
				cookie['role']['max-age'] = timeout

				print cookie
				print "location: owner.cgi\n"
				break
			if(row[0] == 'Visitor'):

				cookie = Cookie.SimpleCookie()
				
				cookie['user'] = user
				cookie['role'] = 'Visitor'

				cookie['user']['max-age'] = timeout
				cookie['role']['max-age'] = timeout
				print cookie
				print 'location: galleryv.cgi\n'
				break
		print 'content-type:text/html\n\n'
		print """<html><head><link rel = 'stylesheet' type = 'text/css' href = 'style.css'>
				<title>Invalid Password</title></head><body>
				<div class = 'edit'>
				<h3>Invalid Password</h3>
				<form action = 'login.html'>
				<input type = 'submit' value = 'Try Again'></input>
				</form>
				</div>
				</body></html>"""
		break


else:

		print 'content-type:text/html\n\n'
		print """<html><head><link rel = 'stylesheet' type = 'text/css' href = 'style.css'>
				<title>User Not Found</title></head><body>
				<div class = 'edit'>
				<h3>User Not Found</h3>
				<form action = 'login.html'>
				<input type = 'submit' value = 'Try Again'></input>
				</form>
				</div>
				</body></html>"""
		









