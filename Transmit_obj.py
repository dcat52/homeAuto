import threading
import Queue
from time import sleep
import subprocess

DEVICES = { \
	"tw" : {"on" : "87347", "off" : "87356"}, \
	"li" : {"on" : "1", "off" : "0"}}

class Transmit(threading.Thread):
	def __init__(self, queue):
		print "Transmit begun"
		threading.Thread.__init__(self)
		self.queue = queue
		
	def stop(self):
		print "killing Transmit"
		self.join()
		
	def getCode(self):
		print "Transmit waiting on code"
		item,state = self.queue.get()
		send(DEVICES[item][state])
		
	def send(self, code):
		print "Sending code", code
		subprocess.call(["/var/www/rfoutlet/codesend", code])
		sleep(0.2)
		getCode()