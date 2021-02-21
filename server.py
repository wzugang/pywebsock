#coding=utf-8

import socket
import time
import datetime
#datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
import select
import threading

host = '' #support all address
port = 80
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(5)
s.setblocking(False)

read_list=[s]
write_list=[]
error_list=[s]
#conn,addr = s.accept()
#print 'connected by ',addr

#def timer_func(arg, kargs):
def timer_func(fd):
	print "fd : ", fd #如果加了逗号,不换行
	#print "kargs :", kargs
	try:
		print "sendall start : ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
		fd.sendall("notify")
		print "sendall end : ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
	except socket.error, e:
		err = e.args[0]
		if err == errno.EAGAIN or err == errno.EWOULDBLOCK:
			pass
		else:
			print "sendall error : ", datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
			print e
			print err
		pass

while True:
	readable_list, writable_list, exceptional_list = select.select(read_list, write_list, error_list, 1) #1为超时时间
	for fd in readable_list:
		if fd is s:
			conn, addr = fd.accept()
			print "\n",'connected by ',addr
			conn.setblocking(False)
			read_list.append(conn)
			error_list.append(conn)
		else:
			try:
				data = fd.recv(1024)
			except socket.error, e:
				print "server recv error : ", fd
				if fd in read_list:
					read_list.remove(fd)
				if fd in write_list:
					write_list.remove(fd)
				if fd in error_list:
					error_list.remove(fd)
				fd.close()
				print e
				continue
			if data != '':
				print "received : ", data
				if "subs" == data:
					write_list.append(fd)
			else:
				print datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f"), "server close : ", fd
				if fd in read_list:
					read_list.remove(fd)
				if fd in write_list:
					write_list.remove(fd)
				if fd in error_list:
					error_list.remove(fd)
				fd.close()
	
	for fd in writable_list:
		print "writable_list : ",writable_list
		if fd in write_list:
			write_list.remove(fd)
		#timer = threading.Timer(1, timer_func, (fd,), {"test":"abc"})
		timer = threading.Timer(0, timer_func, (fd,))
		timer.start()
		#raise error(EBADF, 'Bad file descriptor')
		#error: [Errno 9] Bad file descriptor
		
		
	for fd in exceptional_list:
		print "exceptional_list : ",exceptional_list
		print "error conn : ", fd.getpeername()
		if fd in read_list:
			read_list.remove(fd)
		if fd in write_list:
			write_list.remove(fd)
		if fd in error_list:
			error_list.remove(fd)
		fd.close()
	#data = conn.recv(1024)
	#if not data:
	#	break
	#if "subs" == data:
	#	while True:
	#		time.sleep(3)
	#		conn.sendall("notify")
	#conn.sendall(data)
s.close()









