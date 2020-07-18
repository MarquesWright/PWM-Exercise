import RPi.GPIO as GPIO
import time

# configure the Pi to use the BCM pin names
GPIO.setmode(GPIO.BCM)

# variables that store the pin locations on the GPIO
red_led = 18
green_led = 23
blue_led = 24

# setting up GPIO pins to be an output 
GPIO.setup(red_led, GPIO.OUT)
GPIO.setup(green_led, GPIO.OUT)
GPIO.setup(blue_led, GPIO.OUT)

# 
pwmRed = GPIO.PWM(red_led, 500)
pwmRed.start(0)

pwmGreen = GPIO.PWM(green_led, 500)
pwmGreen.start(0)

pwmBlue = GPIO.PWM(blue_led, 500)
pwmBlue.start(0)

# a list to control the level of brightness
duty = list(range(0, 100))


try:
    while True:

        # for loops for the red color in the LED
        for d in duty:
            pwmRed.ChangeDutyCycle(d)
            time.sleep(0.1)
        
        for dd in reversed(duty):
            pwmRed.ChangeDutyCycle(dd)
            time.sleep(0.1)

        # a pause in the lighting and dimming of the red LED
        time.sleep(1.0)
        
        # for loops for the green color in the LED
        for d in duty:
            pwmGreen.ChangeDutyCycle(d)
            time.sleep(0.1)

        for dd in reversed(duty):
            pwmGreen.ChangeDutyCycle(dd)
            time.sleep(0.1)

        # a pause in the lighting and dimming of the green LED
        time.sleep(1.0)

        # for loops for the blue color in the LED
        for d in duty:
            pwmBlue.ChangeDutyCycle(d)
            time.sleep(0.1)

        for dd in reversed(duty):
            pwmBlue.ChangeDutyCycle(dd)
            time.sleep(0.1)

        # a pause in between PWD and Blinking
        time.sleep(1.0)

        
        GPIO.output(red_led, True)      # red LED on
        time.sleep(0.5)                 # delay 0.5 seconds
        GPIO.output(red_led, False)     # red LED off
        time.sleep(0.5)                 # delay 0.5 seconds

        GPIO.output(green_led, True)    # green LED on
        time.sleep(0.5)                 # delay 0.5 seconds
        GPIO.output(green_led, False)   # green LED off
        time.sleep(0.5)                 # delay 0.5 seconds

        GPIO.output(blue_led, True)     # blue LED on
        time.sleep(0.5)                 # delay 0.5 seconds
        GPIO.output(blue_led, False)    # blue LED off
        time.sleep(0.5)                 # delay 0.5 seconds

            

finally:
    print("Cleaning up")
    GPIO.cleanup()
