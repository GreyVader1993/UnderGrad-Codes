import socket

serversocket = socket.socket()
host = socket.gethostname()
port = 8888

print "Server1 started at host:"+str(host)+" and port:"+str(port)


serversocket.bind((host,port))
serversocket.listen(1)

multiplicand = 2

while True:
	conn, addr = serversocket.accept()
	print "Connected to client:",addr
	conn.send(str(multiplicand))
	print "Success: Multiplicand send !"
	conn.close()