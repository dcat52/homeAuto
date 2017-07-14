# homeAuto
from Dweet_obj import Dweet
from Transmit_obj import Transmit
from time import sleep

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
	
	while threading.active_count() > 0:
		sleep(0.1)

if __name__ == "__main__":
	main()


dweeter.stop()
transmitter.stop()
print "All Dead"