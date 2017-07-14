# homeAuto
from Dweet_obj import Dweet
from Transmit_obj import Transmit

import threading
import Queue
from time import sleep

def main():
	print "Main begun"
	queue = Queue.Queue()
	
	dweeter = Dweet(queue)
	transmitter = Transmit(queue)
	dweeter.start()
	transmitter.start()
	
	try:
		while threading.active_count() > 0:
    		time.sleep(0.1)
		
if __name__ == "__main__":
	main()


dweeter.stop()
transmitter.stop()
print "All Dead"