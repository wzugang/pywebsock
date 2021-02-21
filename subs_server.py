#coding=utf-8

import socket
import time
import datetime
#datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
import select
import threading
import selectors2 as selectors
#pip install selectors
#ImportError: No module named selectors
#python -m pip install --upgrade pip
#python -m pip install --upgrade pip==19.3
#python -m pip -V
#pip install selectors2



class subs_server:
	def __init__(self, port):
		self.port = port
		self.selector = selectors.DefaultSelector()
		self.sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.start = False
	
	def accept(self, sock, mask):
		conn, addr = sock.accept()
		conn.setblocking(False)
		self.selector.register(conn, selectors.EVENT_READ, self.read)
	
	def read(self, conn, mask):
		data = conn.recv(1024)  # 数据理应已可就绪
		if data:
			print data
			if "subs" == data:
				conn.sendall("notify")
		else:
			self.selector.unregister(conn)
			conn.close()
	
	def start_server(self):
		self.sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
		self.sock.bind(('', self.port))
		self.sock.listen(100)
		self.sock.setblocking(False)
		self.selector.register(self.sock, selectors.EVENT_READ, self.accept)
		self.start = True
		while self.start:
			events = self.selector.select()
			for key, mask in events:
				callback = key.data
				callback(key.fileobj, mask)
		self.sock.close()
	
	def stop_server(self):
		self.start = False
		#self.sock.close()

try:
	subs = subs_server(80)
	subs.start_server()
except KeyboardInterrupt:
	subs.stop_server()











