# 🌟 PicoBot Afterschool Lesson Plan

**Audience:** 7th & 8th Grade Girls  
**Purpose:** Spark interest in robotics, build confidence, and introduce hands-on coding and electronics using the Raspberry Pi Pico (via PicoBot).  
**Duration:** 3 Sessions (1 hour each)

---

## 📅 Overview

| Session | Theme                         | Focus                                     |
|--------|-------------------------------|-------------------------------------------|
| 1      | Meet the Pi & Python          | Hello World, Blinking LED, GPIO Basics    |
| 2      | Inputs & Outputs              | Button + LED Control                      |
| 3      | Meet the PicoBot              | Motor Control, Movement Routines          |

---

## 🧭 Session 1: Let's Get Started with Raspberry Pi & Python!

**Theme:** _“You’ve got the power — Let’s talk to a robot!”_  

### Objectives:
- Understand what a Raspberry Pi Pico is
- Write a basic Python program
- Blink an onboard LED
- Learn what GPIO means

### Activities:
- **Welcome & Icebreaker** (10 min)  
  _Prompt: “What’s one thing you’d love to make a robot do?”_
- **What is Raspberry Pi Pico?** (10 min)  
  - Microcontroller vs. computer
  - Show board parts (USB, pins)
- **Python Hello World** (15 min)  
  - Open Thonny
  - Type: `print("Hello, World!")`
- **Blink an LED** (40 min)  
  - Use onboard LED or wire external one
  - Modify blink speed or color

### Sample Code:
```python
from machine import Pin
import time

led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    time.sleep(0.5)
