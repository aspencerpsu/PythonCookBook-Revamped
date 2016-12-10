from httplib import HTTPConnection
import threading
import logging
import semaphore

logging.basicConfig(level=logging.INFO, format="(%(threadName)-10s) %(message)s", )
def save(html, file_absolute_path):
	logging.info("saving {} bytes to {}".format(len(html), file_absolute_path))
	with open(file_absolute_path, 'wb+') as file:
		file.write(html)
		file.flush()

def crawl(req):
	logging.info("executing get request for parameters: {}".format(str(req)))
	connection = HTTPConnection(req["host"], req["port"])
	connection.request("GET", req["path"])
	response = connection.getresponse()
	logging.info("got {} response http code".format(response.status))
	logging.debug("headers: {}".format(str(response.getheaders)))
	response_content = response.read()
	logging.debug("actual response: {}".format(response_content))
	return response_content

class MyCrawler(threading.Thread):
	def __init__(self, req, file_path):
		threading.Thread.__init__(self, name="Crawler-{}".format(req["host"]))
		self.req = req
		self.file_path = file_path

	def run(self):
		global executed_crawlers
		html = crawl(self.req)
		save(html, self.file_path)
def __main__():
	continue_input = True
	threads = []
	while continue_input:
		host = input("host: ")
		port = 80 # int(input("port: "))
		path = "/" # input("path: ")
		file_path = input("output file absolute path: ")
		req = {"host": host, "port": port, "path": path}
		threads.append(MyCrawler(req, file_path))
		continue_input = input("add another? (y/N) ") == "y"
	for t in threads:
		t.start()
		# t.join()
__main__()

