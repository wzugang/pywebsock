# !usr/bin/env python
# -*- coding:utf-8 _*-
"""
@Author:���Խ���
@Blog(���˲��͵�ַ): shuopython.com
@WeChat Official Account(΢�Ź��ں�)��Գ˵python
@Github:www.github.com
 
@File:python_.py
@Time:2019/10/21 21:25
 
@Motto:�����Ͳ�������ǧ�����С�����Գɽ��������������ľ�����Ҫ��ֲ�и�ػ��ۣ�
"""
 
# �����߳�ģ��
import threading
 
# ������������condition
con = threading.Condition()
 
def thread_one(name):
	# ��������condition �߳�����
	con.acquire()
 
	print("{}:�������׼��������".format(name))
	# �������ڵȴ�(wait)���߳�
	con.notify()
 
	# �ȴ��Է���Ӧ��Ϣ��ʹ��wait�����̣߳��ȴ��Է�ͨ��notify���ѱ��߳�
	con.wait()
	print("{}:һ�ɶ���".format(name))
 # ���ѶԷ�
	con.notify()
 
 # �ȴ���Ϣ��Ӧ
	con.wait()
	print("{}:һ���֪����������Ů�����������򵥵�ģ����ˣ�ë��ë��".format(name))
	# ���ѶԷ�
	con.notify()
 
	# �ȴ���Ϣ��Ӧ
	con.wait()
	print("{}:ӴӴӴ��������".format(name))
	# ���ѶԷ�
	con.notify()
 
	# ��������condition �߳��ͷ���
	con.release()
 
def thread_two(name):
	# ��������condition �߳�����
	con.acquire()
 
	# wait����״̬���ȴ������߳�ͨ��notify���ѱ��߳�
	con.wait()
	print("{}:׼������~��ʼ�ɣ�".format(name))
	# ���ѶԷ�
	con.notify()
 
	# �ȴ���Ϣ��Ӧ
	con.wait()
	print("{}:�����ð���û����...�����򵥵��...".format(name))
	# ���ѶԷ�
	con.notify()
 
	# �ȴ���Ϣ��Ӧ
	con.wait()
	print("{}:��,�����֪������̤ʵ��".format(name))
	# ���ѶԷ�
	con.notify()
 
	con.release()
 
if __name__ == "__main__":
 
	# ��������ʼ���߳�
	t1 = threading.Thread(target=thread_one,args=("A"))
	t2 = threading.Thread(target=thread_two,args=("B"))
 
	# �����߳� -- ע���߳�����˳������˳�����Ҫ
	t2.start()
	t1.start()
 
	# �������̣߳��ȴ����߳̽���
	t1.join()
	t2.join()
 
	print("���������")

 
 
 