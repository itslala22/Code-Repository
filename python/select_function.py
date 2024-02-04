# case 01
import select
import socket
import sys
import Queue
 
# Create a TCP/IP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setblocking(0)
 
# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
server.bind(server_address)
 
# Listen for incoming connections
server.listen(5)


# case02
import pymysql

# connect to databse
db = pymysql.connect(host='localhost',port=3306,user='root',password='password',database='database_name')
# get cursor
cur = db.cursor()
cur.execute('SELECT * FROM table_name')
# outcome
results = cur.fetchall()
# end
cur.close()
db.close()


# select function
cur.execute('SELECT * FROM table_name')
results = cur.fetchall()

cur.execute('SELECT name FROM table_name')
results = cur.fetchall()

cur.execute('SELECT * FROM table_name WHERE name='John'')
results = cur.fetchall()
