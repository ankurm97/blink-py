import RPi.GPIO as g
from time import sleep
g.setmode (g.BCM)
g.setup (18, g.OUT)
while 1:
	g.output (18, 1)
	sleep(1)
	g.output(18, 0)
	sleep(1)
