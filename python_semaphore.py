#coding=utf-8

import threading,time,random

#BoundedSemaphore调用时如果计数器的值超过了初始值会抛出异常;但是Semaphore不会
#semaphore=threading.Semaphore(3)#同一时间只能有3个线程处于运行状态
semaphore=threading.BoundedSemaphore(3)   #同一时间只能有3个线程处于运行状态
def run (ii):
	semaphore.acquire() # 获得信号量:信号量减一
	print(ii,'号车可以进入')
	time.sleep(random.randint(0,10)*1)
	print(ii,'号停车位释放')
	semaphore.release()# 释放信号量:信号量加一
	# 再次释放信号量:信号量加一，这时超过限定的信号量数目会报错ValueError: Semaphore released too many times
	#semaphore.release()

for i in range(5):#创建5个线程
	t=threading.Thread(target=run,args=(i,))
	t.start()
	
	