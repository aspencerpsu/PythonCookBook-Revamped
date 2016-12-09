# The following example was taken from `Python Programming Cookbook From Sebastian Vinci
# It takes on understanding concurrencies and when it is best avisable to utilize joining 
# thread concurrencies, and locking daemons, thread options, and joining threads.
""" The following example is about locking for a purchasing, producing, & labeling
	Thread that makes it aware of creating a lock on the thread, storing it with a key
		and until the thread is finished upon completion, releasing the lock, BUT ONLY
	UNTIL the key was generated and aquired upon request"""

import random
import threading
import logging
import time
from time import clock

logging.basicConfig(level=logging.INFO,
				format="[%(levelname)s] (%(threadName)-s) (%(module)-s) (%(funcName)-s) %(message)s", filename="/tmp/locking-py.log")

class Repository:
	def __init__(self):
		self.repo = {}
		self.lock = threading.Lock()
		self.process = clock
	
	def create(self, entry):
		logging.info("waiting for lock")
		with self.lock:
			logging.info("acquired lock within %f seconds"%(self.process()))
			new_id = len(self.repo.keys())
			entry["id"] = new_id
			self.repo[new_id] = entry
	
		################ No longer required to acquire the lock creation with
		################ the `with` command
		################ under new threading module
	
		#self.lock.acquire()
		#try:
			#logging.info("acquired lock")
			#new_id = len(self.repo.keys())
			#entry["id"] = new_id
			#self.repo[new_id] = entry
		#finally:
			#logging.info("releasing lock")
			#self.lock.release()
	
	def find(self, entry_id):
		logging.info("waiting for lock")
		with self.lock:
			try:
				logging.info("acquired lock in %f seconds"%(self.process()))
				return self.repo[entry_id]
			except KeyError:
				return None
		######### Read notes above ################
			#finally:
			#logging.info("releasing lock")
			#self.lock.release()
	def all(self):
		logging.info("waiting for lock")
		with self.lock:
			#try:
			logging.info("acquired lock in %f seconds"%(self.process()))	
			return self.repo
		##### Once Again The Lock Is Self-Explanatory #####
		##### With The `with` command #####
		#finally:
			#logging.info("releasing lock")
			#self.lock.release()
	
class ProductRepository(Repository):
	def __init__(self):
		Repository.__init__(self)
	
	def add_product(self, description, price):
		self.create({"description": description, "price": price})

class PurchaseRepository(Repository):
	def __init__(self, product_repository):
		Repository.__init__(self)
		self.product_repository = product_repository

	def add_purchase(self, product_id, qty):
		product = self.product_repository.find(product_id)
		if product is not None:
			total_amount = product["price"] * qty
			self.create({"product_id":product_id, "qty":qty, "total_amount":total_amount})
	
	def sales_by_product(self, product_id):
		sales = {"product_id": product_id, "qty": 0, "total_amount": 0}
		all_purchases = self.all()
		for k in all_purchases:
			purchase = all_purchases[k]
			if purchase["product_id"] == sales["product_id"]:
				sales["qty"] += purchase["qty"]
				sales["total_amount"] += purchase["total_amount"]
			return sales

class Buyer(threading.Thread):
	def __init__(self, name, product_repository, purchase_repository):
		threading.Thread.__init__(self, name="Buyer-" + name)
		self.product_repository = product_repository
		self.purchase_repository = purchase_repository
	
	def run(self):
		for i in range(0, 1000):
			max_product_id = len(self.product_repository.all().keys())
			product_id = random.randrange(0, max_product_id + 1, 1)
			qty = random.randrange(0, 100, 1)
			self.purchase_repository.add_purchase(product_id, qty)

class ProviderAuditor(threading.Thread):
	def __init__(self, product_id, purchase_repository):
		threading.Thread.__init__(self, name="Auditor-product_id" + str(product_id))
		self.product_id = product_id
		self.purchase_repository = purchase_repository
		self.semaphore = threading.Semaphore(3)
	
	def run(self):
		with self.semaphore:
			logging.info(str(self.purchase_repository.sales_by_product(self.product_id)))


def __main__():
	product_repository = ProductRepository()
	purchase_repository = PurchaseRepository(product_repository)

	input_another_product = True
	while input_another_product:
		description = str(input("product description: "))
		price = float(input("product price: "))
		product_repository.add_product(description, price)
		input_another_product = str(input("continue (y/N): ")) == "y"
	buyers = [Buyer("carlos", product_repository, purchase_repository),
	Buyer("Juan", product_repository, purchase_repository),
	Buyer("Mike", product_repository, purchase_repository),
	Buyer("Sarah", product_repository, purchase_repository),]
	for b in buyers:
		b.start()
		b.join()
	for i in product_repository.all():
		ProviderAuditor(i, purchase_repository).start()


__main__()
