#coding=utf-8

import threading
#�߳����¼�������Ҳ���¼�

#�¼�Event��Ҫ���ڻ������������ȴ�״̬���߳�;

#set() �� ȫ�����ñ�־Flag������־Flag ����Ϊ True,֪ͨ�ڵȴ�״̬(wait)���ָ̻߳�����;
#isSet() �� ��ȡ��־Flag��ǰ״̬������True ���� False;
#wait() �� һ�����ã��߳̽��ᴦ������״̬��ֱ���ȴ������̵߳���set()�����ָ�����;
#clear() �� ����־����ΪFalse��
#�¼�event����һ��ȫ�����ñ�־Flag��ֵΪ True ����False��ʹ��wait()�������̻߳ᴦ������״̬,��ʱFlagָΪFalse��
#ֱ���������̵߳���set()������ȫ�ֱ�־Flag��ΪTrue�����������߳����ָ̻����У���������isSet()������鵱ǰ��Flag״̬.

eEvent = threading.Event()

def get_girl_friend(id):
	print("����{}��׼����ϣ�����Flag״̬��{}.....".format(id, eEvent.isSet()))
	eEvent.wait()
	print("����%d�����....."%id)

if __name__ == "__main__":
	thread_list = list()
	for i in range(1,11):
		# ��������ʼ���߳�
		t = threading.Thread(target=get_girl_friend,args=(i,))
		# �����߳�
		t.start()
		# ���߳̾�����list�б���
		thread_list.append(t)
	# �����߳�׼����ϣ���event����Flag����ΪTrue,�ָ������������߳�
	eEvent.set()
	# �����б��������߳�
	for t in thread_list:
		# �������̣߳��ȴ��������߳̽���
		t.join()
	print("���������")


