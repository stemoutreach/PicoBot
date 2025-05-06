
# 🧠 Raspberry Pi Robotics Worksheet: Controlling Motors with L298N

**Objective:**  
Learn how to control two DC motors using Python and a Raspberry Pi Pico with the L298N motor driver.

---

## 🔌 Wiring Summary

| Component | L298N Output | GPIO Pin |
|----------|---------------|----------|
| Motor A - IN1 | OUT1 | GP6 |
| Motor A - IN2 | OUT2 | GP7 |
| Enable A | ENA | GP8 |
| Motor B - IN3 | OUT3 | GP4 |
| Motor B - IN4 | OUT4 | GP3 |
| Enable B | ENB | GP2 |

---

## 🧱 Starter Code

Copy and run the starter code below. Your task will be to write your own movement functions.

```python
from machine import Pin
import time

# Setup motor pins
In1 = Pin(6, Pin.OUT)
In2 = Pin(7, Pin.OUT)
EN_A = Pin(8, Pin.OUT)

In3 = Pin(4, Pin.OUT)
In4 = Pin(3, Pin.OUT)
EN_B = Pin(2, Pin.OUT)

# Turn on motors
EN_A.high()
EN_B.high()

# Move Forward
def move_forward():
    In1.high()
    In2.low()
    In3.high()
    In4.low()

# Stop
def stop():
    In1.low()
    In2.low()
    In3.low()
    In4.low()

# TODO: Write your own functions below!

def move_backward():
    # Add code here
    pass

def turn_left():
    # Add code here
    pass

def turn_right():
    # Add code here
    pass

# Try it out!
move_forward()
time.sleep(2)
stop()
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
