from machine import Pin
import time

# Motor Pins
In1 = Pin(6, Pin.OUT)
In2 = Pin(7, Pin.OUT)
EN_A = Pin(8, Pin.OUT)

In3 = Pin(4, Pin.OUT)
In4 = Pin(3, Pin.OUT)
EN_B = Pin(2, Pin.OUT)

# Enable the motors
EN_A.high()
EN_B.high()

# LED and buzzer
led = Pin(28, Pin.OUT)
buzzer = Pin(10, Pin.OUT)

# Motor functions
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