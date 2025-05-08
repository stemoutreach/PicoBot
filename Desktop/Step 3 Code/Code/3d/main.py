from machine import Pin
import time
import robot_utils  # This brings in all the functions

# Setup button
button = Pin(14, Pin.IN, Pin.PULL_UP)  # Button connected to GND

print("Press the button to reverse and beep!")

while True:
    if button.value() == 0:  # Button pressed
        robot_utils.move_backward()
        time.sleep(1)
        robot_utils.stop_motors()
        time.sleep(0.5)