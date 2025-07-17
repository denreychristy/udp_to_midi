# UDP To MIDI: Test Server

# ==================================================================== #

import socket
from random import randint
from time import sleep

# ==================================================================== #

UDP_IP = "127.0.0.1"
UDP_PORT = 5005
SOCKET = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

for _ in range(10):
	if randint(1, 10) > 1:
		c = randint(0, 15)
		n = randint(0, 127)
		v = randint(0, 127)
		message = f"{{'channel': {c}, 'note': {n}, 'value': {v}}}"
	else:
		message = f"lol"
	
	message = message.encode(encoding = "utf-8")
	SOCKET.sendto(message, (UDP_IP, UDP_PORT))
	sleep(1)

SOCKET.close()