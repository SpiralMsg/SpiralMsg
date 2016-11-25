#! /usr/bin/python

import os
import socket
import sys

host = "localhost"
port = 50000
backlog = 2
maxsize = 1024

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen(backlog)

client1, client1_address = server.accept()
client1.sendall("Waiting for partner...")

client2, client2_address = server.accept()
client2.sendall("Waiting for partner...")

client1.sendall("Partner connected.")
client2.sendall("Partner connected.")

pid = os.fork()

if pid == 0:
	while True:
		data = client1.recv(maxsize)
		client2.sendall("From %s: " % str(client1_address) + data)
elif pid > 0:
	while True:
		data = client2.recv(maxsize)
		client1.sendall("From %s: " % str(client2_address) + data)




