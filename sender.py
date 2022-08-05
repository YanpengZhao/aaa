import socket
import os
import struct
from sys import argv

import socket


recv_ip = "127.0.0.1"
recv_port = 4096
s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
while 1:
	while 1:
		msg = b'i am a man'
		if len(msg)>150:
			print("Message length exceeded ")
		else :
			break
	s.sendto(msg,(recv_ip,recv_port))
	if msg=='exit':
		s.close()
		break
	data=s.recvfrom(150)
	if str(data[0]) == 'exit':
		print("EXIT")
		s.close()
		break
	else:		
		print("RECEIVED PACKET: "+str(data[0]))
