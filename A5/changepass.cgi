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
	print 'Location: login.html'

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


query = 'update Users set Password = ' + "'" + password + "'" + ' where Name = ' + "'" + user + "'"

db = MySQLdb.connect(host='egon.cs.umn.edu', user=uid, passwd=dbpassword, port=3307)

db.select_db(uid)

cursor = db.cursor()

cursor.execute(query)

db.commit()

print 'location: owner.cgi\n'