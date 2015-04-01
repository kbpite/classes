"""
FLIGHT SIMULATOR v0.2

* plane changes its position randomly because of the wind
* the change can be either to the left or to the right
* the change has to be within range <-15,15>
* minus means LEFT, plus means RIGHT

* there is a position corrector, which tries to stabilize the plane
* it performs a random number of corrections, trying to approach 0

* CTRL+C will gracefully finish the simulation
"""

from random import randint, choice
from time import sleep
from sys import exit

def get_direction(degrees):
	if degrees == 0:
		return 'BALANCED'
	return 'LEFT' if degrees < 0 else 'RIGHT'

def check_termination():
	pass

def iterate():
	check_termination()	
	sleep(1)

class PositionCorrector:
	@staticmethod
	def correct(position):
		''' Corrects given position random amount of times '''
		n = randint(1,15)
		while n != 0 and position != 0:
			correction = 1 if position < 0 else -1
			position = position + correction
			print 'Position corrected. Current position: ' + str(position) + ' (' + get_direction(position) + ')'
			n = n - 1
			iterate()
		return position

class RandomChanger:
	@staticmethod
	def change(position):
		degrees = randint(-15,15)
		position = position + degrees
		print 'Position changed: ' + str(degrees) + '. Current position: ' + str(position) + ' (' + get_direction(degrees) + ')'
		iterate()
		return position

def main():
	position = 0
	print 'Starting position: 0 degrees'

	try:
		while True:
			position = RandomChanger.change(position)
			position = PositionCorrector.correct(position)
	except KeyboardInterrupt:
		print '\nSIMULATION FINISHED!'

main()

