
# 🧠 Raspberry Pi Robotics Worksheet: Controlling Motors with L298N

**Objective:**  
Learn how to control two DC motors using Python and a Raspberry Pi Pico with the L298N motor driver.

---

## 🔌 Wiring Summary

| Component        | L298N Output | GPIO Pin |
|------------------|---------------|----------|
| Motor A - IN1     | OUT1          | GP6      |
| Motor A - IN2     | OUT2          | GP7      |
| Enable A          | ENA           | GP8      |
| Motor B - IN3     | OUT3          | GP4      |
| Motor B - IN4     | OUT4          | GP3      |
| Enable B          | ENB           | GP2      |

---

## 🧱 Starter Code with Comments

```python
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
```

---

## ✍️ Challenges

1. **Write the `move_backward()` function.**  
   - Hint: Reverse both motors by flipping the `.high()` and `.low()` values.

2. **Write the `turn_left()` function.**  
   - Hint: You could stop the right motor, or reverse the right motor and keep the left moving forward.

3. **Write the `turn_right()` function.**  
   - Hint: Try the opposite of your `turn_left()` function.

---

## ✅ Reflection Questions

- What happens when both motors spin in the same direction?
- What happens when one motor spins forward and the other spins backward?
- What could go wrong if both direction pins (IN1 and IN2) are set to HIGH at the same time?

---

Happy Coding! 🤖
