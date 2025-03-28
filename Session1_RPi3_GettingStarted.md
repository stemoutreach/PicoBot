# 🧭 Session 1: Let's Get Started with Raspberry Pi & Python!

**Theme:** _“You’ve got the power — Let’s talk to a robot!”_

## Objectives:
- Understand what a Raspberry Pi 3 is
- Write a basic Python program
- Blink an LED using GPIO
- Learn what GPIO means

## Activities:
### 1. Welcome & Icebreaker (10 min)
Prompt: “What’s one thing you’d love to make a robot do?”

### 2. What is Raspberry Pi 3? (10 min)
- Small computer vs. microcontroller
- Show ports (USB, HDMI, GPIO pins)

### 3. Python Hello World (15 min)
- Open Thonny (or use IDLE)
- Type: `print("Hello, World!")`

### 4. Blink an LED (40 min)
- Connect LED to GPIO using breadboard
- Modify blink speed or color if using RGB LED

## Sample Code (requires RPi.GPIO):
```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)

while True:
    GPIO.output(18, GPIO.HIGH)
    time.sleep(0.5)
    GPIO.output(18, GPIO.LOW)
    time.sleep(0.5)
```
