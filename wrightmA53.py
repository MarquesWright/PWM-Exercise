# import the Sense Hat emulator module
from sense_emu import SenseHat
import time


# create a SenseHat object
sense = SenseHat()

# print out the temperature, humidity, atmospheric pressure,
# and raw accelerometer from the SenseHat emulated sensors
print('The temperature is ',sense.get_temperature(),'degrees Celsius')
print('The humidity is ',sense.get_humidity(),'%')
print('The atmospheric pressure is ',sense.get_pressure(),'millibars')
print('The raw accelerometer data is ',sense.get_accelerometer_raw())


sense.show_message('Marques',scroll_speed=0.1, text_colour=[255,69,0])


w = (200, 200, 200) # the color white
p = (102, 0, 153)   # the color purple

letter = [
    w, w, w, w, w, w, w, w,
    w, p, p, p, p, p, w, w,
    w, p, w, w, w, w, p, w,
    w, p, w, w, w, w, p, w,
    w, p, p, p, p, p, w, w,
    w, p, w, w, p, w, w, w,
    w, p, w, w, w, p, w, w,
    w, p, w, w, w, w, p, w
    ]

sense.set_pixels(letter)
time.sleep(5.0)
