import RPi.GPIO as gpio 
import time.sleep as delay 

gpio.setmode(gpio.BCM)
gpio.setup(17, gpio.OUT)
gpio.setup(22, gpio.OUT)
gpio.setup(27, gpio.OUT)
gpio.setup(18, gpio.OUT)

def seq(a1, a2, b1, b2):
  gpio.output(17, a1)
  gpio.output(22, a2)
  gpio.output(27, b1)
  gpio.output(18, b2)

while True:
  try:
    seq(1, 0, 0, 0) # Coil 1 energized coil 2 cutoff
    delay(0.010)
    seq(0, 0, 1, 0) # Coil1 cutoff coil 2 energized
    delay(0.010)
    seq(0, 1, 0, 0) # Coil 1 energized with flipped polarity and coil 2 is cutoff
    delay(0.010)
    seq(0, 0, 0, 1) # Coil 2 energized with flipped polarity and coil 1 is cutoff
    delay(0.010)
  except KeyboardInterrupt:
    gpio.cleanup()
    break