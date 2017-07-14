import threading
import Queue
from time import sleep
import dweepy
import json
from collections import namedtuple

DWEET_STREAM = 'dscnasa'
FAIL_SLEEP = 1.1

class Dweet(threading.Thread):
	def __init__(self, queue):
		print "Dweet begun"
		threading.Thread.__init__(self)
		self.queue = queue
		self.failCount = 0
		
	def stop(self):
		print "killing Dweet"
		self.join()
		
	def newDweet(self, dweet):
		# parse dweet
		print "Dweet received data"
		jstr = json.dumps(dweet)
		obj = json2obj(jstr)
		print "Dweet object put in queue"
		self.queue.put(obj)
		
	def pullDweets(self):
		# dweet stream
		
		try:
			for dweet in dweepy.listen_for_dweets_from(DWEET_STREAM):
				print dweet
				self.newDweet(dweet)
		
		except Exception, e:
			self.failCount += 1
			print "Total failCount:", self.failCount
			sleep(FAIL_SLEEP)
			pullDweets()

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)