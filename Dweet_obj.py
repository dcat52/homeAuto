from Transmit_obj import Transmit
from time import sleep
import dweepy
import json
from collections import namedtuple

DWEET_STREAM = 'dsctest'
DELAY = 1

class Dweet():
	def __init__(self):
		print "Dweet begun"
		self.transmit = Transmit()
		self.failCount = 0
		self.pullDweets()


	def newDweet(self, dweet):
		# parse dweet
		print "Dweet received data"
		jstr = json.dumps(dweet)
		obj = json2obj(jstr)
		data = (str(obj.content.item), str(obj.content.set))
		print "sending data to transmit"
		self.transmit.getCode(data)
		
	def pullDweets(self):
		# dweet stream
		
		sleep(DELAY)

		try:
			for dweet in dweepy.listen_for_dweets_from(DWEET_STREAM):
				print dweet
				self.newDweet(dweet)
		
		except Exception, e:
			self.failCount += 1
			print "Total failCount:", self.failCount
			self.pullDweets()

def _json_object_hook(d): return namedtuple('X', d.keys())(*d.values())
def json2obj(data): return json.loads(data, object_hook=_json_object_hook)