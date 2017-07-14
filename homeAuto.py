# homeAuto

import threading
import Queue
from time import sleep

def main():
	print "Main begun"
	queue = Queue.Queue()
	
	dweeter = Dweet_obj(queue)
	transmitter = Transmit_obj(queue)
	dweeter.start()
	transmitter.start()
	
	try:
		while True:
			wait =	input("press ctrl+c to kill")
	except KeyboardInterrupt:
		dweeter.stop()
		transmitter.stop()
		
if __name__ == "__main__":
	main()


print "All Dead"