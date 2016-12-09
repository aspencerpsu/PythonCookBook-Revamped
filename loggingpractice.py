import logging
import random


#The following handler should reflect how the methods are designed below

logging_degrees = [{'INFO': 20}, {'DEBUG': 10}, {'ERROR': 40}, {'WARNING': 30}]

for element in logging_degrees:
	logging.basicConfig(level=element.values()[0], format="[%(levelname)s] (%(funcName)s) generated from %(filename)s MESG: %(message)s") 
all_logging_types = [logging.basicConfig(level=element.values()[0], format="[%(levelName)s] (%(funcName)s) generated from %(filename)s MESG: %(message)s") for element in logging_degrees]
print all_logging_types
#logging.basicConfig(format="[%(levelName)s] (%(funcName)s) generated from %(filename)s MESG: %(message)s")
#logging.debug('Some additional information')
#logging.info('Working...')
#logging.warning('Watch out!')
#logging.error('Oh No!')
#logging.critical('x.x')

def check():
	
	try:
		answer = input("What did you think of the movies? ")
		if answer != "Whack":
			logging.info("Working...")
		elif answer == "great":
			logging.debug("Some additional information")
		else:
			logging.info("we can't even try this together")
	except:
		logging.error("You forgot to put the information in strings")

			


check() #run the command
