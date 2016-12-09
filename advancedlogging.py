import csv
import os.path
import logging

logging.basicConfig(level=logging.INFO, 
			format="%(asctime)s - [%(levelname)s] [%(threadName)s] (%(module)s:%(lineno)d) %(message)s", )

class Repository:
	def __init__(self, full_file_path):
		logging.info("initializing contacts repository with file at: {}".format(full_file_path))
		self.full_file_path = full_file_path

	def add(self, contact):
		logging.info("creating contact: {}".format(contact))
		headers = [h for h in contact]
		headers.sort()
		write_headers = not os.path.isfile(
			self.full_file_path) # let's assume no one will go and erase the headers by hand
		with open(self.full_file_path, 'a+') as file:
			writer =csv.DictWriter(file, fieldnames=headers)
			if write_headers:
				logging.debug("this is the first contact in the given file. writing headers.")
				writer.writeheader()
			writer.writerow(contact)
		
	def names(self):
		with open(self.full_file_path, 'r+') as file:
			names = list(map(lambda r: r['name'], csv.DictReader(file)))
			return names

	def full_contact(self, name):
		with open(self.full_file_path, 'r+') as file:
			for contact in list(csv.DictReader(file)):
				if contact['name'] == name:
					return contact
			logging.warning("contact was not found for name: {}".format(name))	
			return

class Main:

	def __init__(self, contacts_file):
		self.repo = Repository(contacts_file)
	
	def create(self):
		name = input("name: ")
		number = input("number: ")
		contact = {"name": name, "number": number}
		self.repo.add(contact)
	
	def names(self):
		names = self.repo.names()
		if len(names) > 0:
		 for n in names:
			print ("- {}".format(n))
		else:
			print("no contacts were found")
	
	def full_contact(self):
		name = input("name: ")
		contact = self.repo.full_contact(name)
		if contact is not None:
			print("name: {}".format(contact["name"]))
			print("number: {}".format(contact["number"]))
		else:
			print "\ncontact not found.\n"
			self.menu()
	
	def menu(self):
		actions = {"1": self.create, "2": self.names, "3": self.full_contact}
		options = ["1) Create Contact", "2) All Contacts", "3) Detail of contact", "0) Exit"]
		for o in options:
			print (o)
		selected = input("What do you want to do? ")
		if selected in actions:
			actions[selected]()
			self.menu()
		else:
			pass

Main("/tmp/contacts.csv").menu()
