#coding=utf-8

import threading
#线程有事件，进程也有事件

#事件Event主要用于唤醒正在阻塞等待状态的线程;

#set() — 全局内置标志Flag，将标志Flag 设置为 True,通知在等待状态(wait)的线程恢复运行;
#isSet() — 获取标志Flag当前状态，返回True 或者 False;
#wait() — 一旦调用，线程将会处于阻塞状态，直到等待其他线程调用set()函数恢复运行;
#clear() — 将标志设置为False；
#事件event中有一个全局内置标志Flag，值为 True 或者False。使用wait()函数的线程会处于阻塞状态,此时Flag指为False，
#直到有其他线程调用set()函数让全局标志Flag置为True，其阻塞的线程立刻恢复运行，还可以用isSet()函数检查当前的Flag状态.

eEvent = threading.Event()

def get_girl_friend(id):
	print("单身狗{}都准备完毕，内置Flag状态：{}.....".format(id, eEvent.isSet()))
	eEvent.wait()
	print("单身狗%d告别单身....."%id)

if __name__ == "__main__":
	thread_list = list()
	for i in range(1,11):
		# 创建并初始化线程
		t = threading.Thread(target=get_girl_friend,args=(i,))
		# 启动线程
		t.start()
		# 将线程句柄添加list列表中
		thread_list.append(t)
	# 所有线程准备完毕，将event内置Flag设置为True,恢复正在阻塞的线程
	eEvent.set()
	# 遍历列表，阻塞主线程
	for t in thread_list:
		# 阻塞主线程，等待所有子线程结束
		t.join()
	print("程序结束！")


