import threading
import time

def my_logic(sleep_time):

	thread_name = threading.current_thread().getName()
	print("{} start".format(thread_name))
	time.sleep(sleep_time)
	print("{} end".format(thread_name))

class MyThread(threading.Thread):

	def __init__(self, sleep_time):
		threading.Thread.__init__(self)
		threading.Thread.__init__(self)
		self.sleep_time = sleep_time
	def run(self):
		my_logic(self.sleep_time)

threads = [MyThread(i) for i in range(1, 4)]
threads[2].setDaemon(True)

for t in threads:
	t.start()
