import logging
import random

from threading import Thread, local

logging.basicConfig(level=logging.INFO,
			format="[%(levelname)s] (%(threadName)-s) (%(module)-s) (%(funcName)-s) %(message)-s",
		     )


def thread(data):
	try:
		logging.info(str(data.value))
	except AttributeError:
		logging.info("data does not have a value yet")

class MyProcess(Thread):
	def __init__(self):
		Thread.__init__(self)
	
	def run(self):
		data = local()
		thread(data)
		data.value = {"process_id": random.randint(0, 1000)}
		thread(data)
	
for i in range(0, 4):
	MyProcess().start()
