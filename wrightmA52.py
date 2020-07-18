import RPi.GPIO as GPIO
import time

# Configure the Pi to recognize the BCM (Broadcom) pin names,
# and not the pin position
GPIO.setmode(GPIO.BCM)

# variable for the pin to be used as a switch
switch_pin = 4

# set up the pin to be an input, and enable an internal pull-up resistor
# on pin 4 to keep the input pulled up high unless connected to a ground
# pin
GPIO.setup(switch_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# declaring a variable to store a value for the number
# of times the switch will be turned on by jumpers
switchcount = 7

# declaring a variable to store the number of times
# the jumpers are connected
response_count = 0

while not response_count == switchcount:
    if GPIO.input(switch_pin) == False:
        print("Power On")
        response_count += 1
        time.sleep(0.5)
