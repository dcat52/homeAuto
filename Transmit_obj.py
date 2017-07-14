from time import sleep
import subprocess

DEVICES = { \
	"tw" : {"on" : "87347", "off" : "87356"}, \
	"li" : {"on" : "1", "off" : "0"}}

class Transmit():
	def __init__(self):
		print "Transmit begun"
		
	def getCode(self, data):
		print "transmit got data"
		print data
		item,state = data
		print item,state
		self.send(DEVICES[item][state])
		
	def send(self, code):
		print "Sending code", code
		subprocess.call(["/var/www/rfoutlet/codesend", code])
		sleep(0.2)