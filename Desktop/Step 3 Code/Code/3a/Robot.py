from machine import Pin        # Lets us control the Pi Pico’s pins
import time                    # Lets us pause the program

# Motor A (connected to OUT1 and OUT2 on the L298N)
In1 = Pin(6, Pin.OUT)          # Sets GPIO 6 as an output for Motor A direction
In2 = Pin(7, Pin.OUT)          # Sets GPIO 7 as an output for Motor A direction
EN_A = Pin(8, Pin.OUT)         # Sets GPIO 8 as output to enable Motor A

# Motor B (connected to OUT3 and OUT4 on the L298N)
In3 = Pin(4, Pin.OUT)          # Sets GPIO 4 as an output for Motor B direction
In4 = Pin(3, Pin.OUT)          # Sets GPIO 3 as an output for Motor B direction
EN_B = Pin(2, Pin.OUT)         # Sets GPIO 2 as output to enable Motor B

# Turn both motors ON by setting enable pins HIGH
EN_A.high()                    # Turns on Motor A
EN_B.high()                    # Turns on Motor B

# Function to move the robot forward
def move_forward():
    In1.high()                 # Motor A spins forward
    In2.low()
    In3.high()                 # Motor B spins forward
    In4.low()

# Function to stop both motors
def stop():
    In1.low()                  # Stop Motor A
    In2.low()
    In3.low()                  # Stop Motor B
    In4.low()

# TODO: Write your own functions below!

def move_backward():
    # Hint: reverse both motors by switching the direction pins
    pass

def turn_left():
    # Hint: try stopping or reversing one motor
    pass

def turn_right():
    # Hint: try the opposite of turn_left
    pass

# Try it out!
move_forward()                 # Move forward
time.sleep(2)                  # Wait for 2 seconds
stop()                         # Stop the robot