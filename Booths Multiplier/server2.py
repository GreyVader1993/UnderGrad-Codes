import socket

serversocket = socket.socket()
host = socket.gethostname()
port = 8889

print "Server2 started at host:"+str(host)+" and port:"+str(port)


serversocket.bind((host,port))
serversocket.listen(1)

multiplier = 4

while True:
	conn, addr = serversocket.accept()
	print "Connected to client:",addr
	conn.send(str(multiplier))
	print "Success: Multiplier send !"	
	conn.close()