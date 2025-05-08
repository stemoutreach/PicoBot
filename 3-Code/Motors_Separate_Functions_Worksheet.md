
# 🧠 Raspberry Pi Robotics: Using Separate Files for Functions

**Objective:**  
Learn how to organize your code better by putting reusable functions (like motor and buzzer control) into a separate file. This helps make your main program shorter and easier to read.

---

## 📂 Project File Structure

You'll create two files:

1. **`robot_utils.py`** – stores all the motor and alert functions  
2. **`main.py`** – runs the robot and uses the functions from `robot_utils.py`

---

## 🧱 `robot_utils.py` (Put This on Your Pico)

```python
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
```

---

## 🧱 `main.py` (Your Main Program)

```python
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
```

---

## ✍️ Challenges

1. Modify `main.py` to use other movement functions (like `turn_left()`).
2. Add a second button for a different action (turn or forward).
3. Try adding a function in `robot_utils.py` called `wiggle()` that turns left and right quickly!

---

## ✅ Reflection Questions

- Why is it helpful to separate functions into a different file?
- Could this help in larger robot projects?
- What happens if you forget to import the file?

---

Start organizing your code like a pro! 📁🦾💡
