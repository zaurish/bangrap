#!/usr/bin/python3
import socket, select, sys

print("Welcome to bangrap v0.1")

try:
	target_ip = input("Select the target IP adress (Ex: 192.168.1.1)--> ")
	first_port = int(input("Select a starting port (0-65535)--> "))
	last_port = int(input("Select the last port (0-65535)--> "))
except:
	print("Incorrect values have been entered")
	sys.exit()
input("Press Enter to start scan")

print("Port: Baner:")
for port in range(first_port,last_port+1):
	print(str(port) + "    ", end="")
	try:
		banner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		banner.connect((target_ip,port))
		to_read = select.select([banner],[],[],1)
		if to_read[0]:
			print(banner.recv(4096))
			banner.close()
		else:
			print("The service did not deliver the banner")
	except:
		print("Failure to get banner")
