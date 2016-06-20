#!/usr/bin/python

import cgi
import cgitb;cgitb.enable()
import MySQLdb
import os


handler = {}
user = ''
cookies = os.environ['HTTP_COOKIE']
cookies = cookies.split(';')
for cookie in cookies:
	cookie = cookie.split('=')
	handler[cookie[0]] = cookie[1]

if 'role' not in handler:
	print 'Location: login.html\n'

else:
	if handler['role'] == 'Visitor':
		print 'Location: galleryv.cgi\n'

form = cgi.FieldStorage()

user = form['user'].value

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

file.close()

db = MySQLdb.connect(host='egon.cs.umn.edu', user=uid, passwd=dbpassword, port=3307)

db.select_db(uid)

cursor = db.cursor()

firstQuery = 'select * from Users where Name = ' + "'" + user + "'"

row_count = cursor.execute(firstQuery)

if(row_count == 0):

	vis = 'Visitor'

	values = "'" + user + "'" + "," + "'" + vis + "'" +  "," + "'" + password + "'" 
	query = 'insert into Users (Name,Role,Password) values(' + values + ')'




	cursor.execute(query)

	db.commit()

	print 'location: owner.cgi\n'

else:
	print 'location: owner.cgi\n'
