# 🧭 Session 1: Let's Get Started with Raspberry Pi & Python!

**Theme:** _“You’ve got the power — Let’s talk to a robot!”_

## Objectives:
- Understand what a Raspberry Pi Pico is
- Write a basic Python program
- Blink an onboard LED
- Learn what GPIO means

## Activities:
### 1. Welcome & Icebreaker (10 min)
Prompt: “What’s one thing you’d love to make a robot do?”

### 2. What is Raspberry Pi Pico? (10 min)
- Microcontroller vs. computer
- Show board parts (USB, pins)

### 3. Python Hello World (15 min)
- Open Thonny
- Type: `print("Hello, World!")`

### 4. Blink an LED (40 min)
- Use onboard LED or wire external one
- Modify blink speed or color

## Sample Code:
```python
from machine import Pin
import time

led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    time.sleep(0.5)
```
