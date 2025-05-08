
# 💡 Raspberry Pi Worksheet: LED, Buzzer, and Button

**Objective:**  
Learn how to control an LED and a buzzer using a button with the Raspberry Pi Pico.

---

## 🔌 Wiring Summary

| Component | Description                | GPIO Pin |
|-----------|----------------------------|----------|
| LED       | Long leg to GPIO via resistor | GP28     |
| Buzzer    | Positive to GPIO           | GP10     |
| Button    | One leg to GPIO, one to GND | GP14     |


<img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/picoWire.jpg" width="600" > 

<img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/Button.jpg" width="600" > 

<img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/Buzzer.jpg" width="600" > 

<img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/LED.jpg" width="600" > 

---

## 🧱 Python Code with Comments

```python
from machine import Pin
import time

# Set up output devices
led = Pin(28, Pin.OUT)         # GP28 controls the LED
buzzer = Pin(10, Pin.OUT)      # GP10 controls the buzzer

# Set up input device (button)
button = Pin(14, Pin.IN, Pin.PULL_UP)  # GP14 reads button state

# Function to turn on alert
def alert_on():
    led.high()                 # Turn on LED
    buzzer.high()              # Turn on buzzer
    print("Alert ON")

# Function to turn off alert
def alert_off():
    led.low()                  # Turn off LED
    buzzer.low()               # Turn off buzzer
    print("Alert OFF")

# Main loop: wait for button press
print("Press the button to turn on the LED and buzzer!")

while True:
    if button.value() == 0:    # Button is pressed
        alert_on()
        time.sleep(0.5)        # Keep alert on briefly
        alert_off()
        time.sleep(0.5)        # Delay to avoid double press
```

---

## ✍️ Challenges

1. **Change how long the alert stays on.** Try adjusting the `time.sleep()` values.
2. **Make it stay on as long as the button is held down.**
3. **Try making the buzzer beep multiple times when the button is pressed.**
4. **Can you make the LED blink while the buzzer is on?**

---

## ✅ Reflection Questions

- What does the `.value()` function do for the button?
- Why do we use `Pin.PULL_DOWN` for the button setup?
- What happens if we connect the button without a pull resistor?

---

Have fun experimenting with electronics! 🔔💡
