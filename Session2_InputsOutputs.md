# 🔌 Session 2: Inputs & Outputs – Buttons, LEDs, and Logic

**Theme:** _“Let’s make your robot listen to you!”_

## Objectives:
- Understand GPIO Input vs Output
- Use buttons to control an LED
- Practice reading digital signals

## Activities:
### 1. Warm-Up Recap (10 min)

### 2. What is GPIO? (10 min)
- Simple whiteboard sketch of signal IN/OUT

### 3. Wire Button + LED (15 min)

### 4. Code Reaction (30 min)
- LED turns on when button is pressed
- Try modifying logic (toggle or inverted)

## Sample Code:
```python
from machine import Pin
import time

led = Pin(15, Pin.OUT)
button = Pin(14, Pin.IN, Pin.PULL_DOWN)

while True:
    if button.value() == 1:
        led.on()
    else:
        led.off()
    time.sleep(0.1)
```
