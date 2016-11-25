#! /usr/bin/python

import readline
import socket
import sys
import thread

def receive_thread():
	while True:
		data = client.recv(maxsize)
		prev_input = readline.get_line_buffer()
		sys.stdout.write("\r" + " " * (len(prev_input) + 2) + "\r")
		print data
		sys.stdout.write("> ")
		if not prev_input.endswith("\n"):
			sys.stdout.write(prev_input)
		sys.stdout.flush()

host = "localhost"
port = 50000
maxsize = 1024

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((host, port))

print client.recv(maxsize)
print client.recv(maxsize)

thread.start_new_thread(receive_thread, ())
while True:
	data = raw_input("> ")
	client.sendall(data)





