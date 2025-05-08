from machine import Pin
import time

# Motor setup
In1 = Pin(6, Pin.OUT)
In2 = Pin(7, Pin.OUT)
EN_A = Pin(8, Pin.OUT)

In3 = Pin(4, Pin.OUT)
In4 = Pin(3, Pin.OUT)
EN_B = Pin(2, Pin.OUT)

EN_A.high()
EN_B.high()

# LED and buzzer setup
led = Pin(28, Pin.OUT)
buzzer = Pin(10, Pin.OUT)

# Button input
button = Pin(14, Pin.IN, Pin.PULL_UP)  # Using internal pull-up, button connected to GND

# Movement functions
def move_forward():
    In1.high()
    In2.low()
    In3.high()
    In4.low()

def move_backward():
    In1.low()
    In2.high()
    In3.low()
    In4.high()

def turn_left():
    In1.low()
    In2.high()
    In3.high()
    In4.low()

def turn_right():
    In1.high()
    In2.low()
    In3.low()
    In4.high()

def stop_motors():
    In1.low()
    In2.low()
    In3.low()
    In4.low()

# Alert functions
def alert_on():
    led.high()
    buzzer.high()
    print("Alert ON")

def alert_off():
    led.low()
    buzzer.low()
    print("Alert OFF")

# Main loop
print("Press the button to move forward with lights and sound!")

while True:
    if button.value() == 0:  # Button pressed (LOW)
        move_forward()
        alert_on()
        time.sleep(1)
        stop_motors()
        alert_off()
        time.sleep(0.5)