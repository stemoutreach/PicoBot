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