import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 305))
serversocket.listen(5)

def something(clientsocket):
	#Do something with the socket
	return None

while True:
	(clientsocket, address) = serversocket.accept()
	something(clientsocket)
