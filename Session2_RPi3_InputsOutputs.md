# 🔌 Session 2: Inputs & Outputs – Buttons, LEDs, and Logic

**Theme:** _“Let’s make your robot listen to you!”_

## Objectives:
- Understand GPIO Input vs Output on Raspberry Pi 3
- Use buttons to control an LED
- Practice reading digital signals

## Activities:
### 1. Warm-Up Recap (10 min)

### 2. What is GPIO? (10 min)
- Simple whiteboard sketch of signal IN/OUT

### 3. Wire Button + LED on Breadboard (15 min)

### 4. Code Reaction (30 min)
- LED turns on when button is pressed
- Try modifying logic (toggle or inverted)

## Sample Code:
```python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(17) == GPIO.HIGH:
            GPIO.output(18, GPIO.HIGH)
        else:
            GPIO.output(18, GPIO.LOW)
        time.sleep(0.1)
except KeyboardInterrupt:
    GPIO.cleanup()
```
