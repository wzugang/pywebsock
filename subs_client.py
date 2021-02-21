#coding=utf-8

import time
import datetime
#datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
import socket
import threading
import select

host = 'localhost'		#remot host
port = 80
#s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#s.connect((host,port))
#s.sendall("subs")
#while True:
#	data = s.recv(1024)
#	print data
#s.close()
#print 'received',repr(data)

def send_cb(sock):
	sock.sendall("subs")
	
def recv_cb(sock):
	try:
		data = sock.recv(1024)
		if '' == data:
			return False
		print data
		return True
	except socket.timeout, e:
		err = e.args[0]
		print e
		print err
	except socket.error, e:
		#print "recv error : ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
		err = e.args[0]
		if err == 'timed out':
			pass
			#print err
		else:
			pass
			#print e
		#pass
		return True

#python socket.error: [Errno 10054]  远程主机强迫关闭了一个现有的连接。


class subs_client:
	def __init__(self, send_cb, recv_cb, host='localhost', port=80):
		self.host = host
		self.port = port
		self.send_cb = send_cb
		self.recv_cb = recv_cb
		self.start = False
		self.thread = None

	def work_cb(self, send_cb, recv_cb):
		sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		sock.connect((self.host, self.port))
		sock.settimeout(1)
		sock.setblocking(False)
		send_cb(sock)
		while self.start:
			#time.sleep(1)
			if not recv_cb(sock):
				break
			
		sock.close()
		print "work_cb end"
	
	def start_work(self):
		self.thread = threading.Thread(target=self.work_cb,args=(self.send_cb, self.recv_cb))
		#self.thread.setDaemon(True) #设置后主线程运行完就会退出（子线程也会退出）,否则主线程会一直等子线程,终端本来就有2个线程
		self.start = True
		self.thread.start()
		
	
	def stop_work(self):
		print "stop work : ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
		self.start = False
		self.thread.join()
	
	
	
try:
	subs = subs_client(send_cb, recv_cb)
	subs.start_work()
	time.sleep(10)
	subs.stop_work()
except KeyboardInterrupt:
	subs.stop_work()
	exit(1)
	
	












