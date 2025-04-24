# Session 1 – Getting Started with the PicoBot

**Goal:** Mount the Pico correctly on the breadboard, configure Thonny, and run a first LED‑blink script.

---

## Learning Objectives

* Orient and seat the Pico WH on a breadboard without bending pins.
* Configure Thonny to use the MicroPython interpreter on the Pico.
* Run a script that blinks the onboard LED.

---

## Materials

| Item | Qty (per student) |
|------|------------------|
| Raspberry Pi Pico WH | 1 |
| Half‑size breadboard | 1 |
| USB‑A ↔ micro‑USB data cable | 1 |
| Pi 500 workstation | 1 |

---
Inside the breadboard

<img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/Insidebread.jpg" width="500" > 


## 1 · Place the Pico on the Breadboard


1. Orient the breadboard like the image below.  
2. Hold the Pico with the **USB port facing the top**.
3. The power rails should be + - on both sides.
4. Align the two rows of header pins over the **center groove**.  
5. Make sure the component rails start with 1 at the top.
6. Press gently until all pins seat flush— Pico pin 1 should be in row 1 column c, pico pin 40 should be in row 1 column h.  

    <img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/PicoPlacement.jpg" width="500" >   
    
> *Tip:* Keep the Pico flush with the top edge of the board—this leaves space for driver wiring below.


---

## 2 · Connect & Configure Thonny

1. Plug the Pico into the Pi 500 using the USB cable (no BOOTSEL needed).  
2. Open **Thonny** → *Tools ▸ Options ▸ Interpreter*.  
3. Select **Interpreter** = **MicroPython (Raspberry Pi Pico)**, **Port** = *Automatic* (or `/dev/ttyACM0`).  
4. Click **OK**. The Shell should show the `>>>` MicroPython prompt.

---

## 3 · Blink the On‑Board LED

```python
from picozero import pico_led
from time import sleep

while True:
    pico_led.on()
    sleep(0.5)
    pico_led.off()
    sleep(0.5)
```

Press ▶️ Run. The small **green LED near the antenna** blinks five times.

## 4 · Blink an LED

1. Plug in the LED to the breadboard - long lead to GPIO 14, short lead to ground (GPIO 13)
2. Load the below
3. Press ▶️ Run.
   
<img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/LEDOnOff.jpg" width="500" >   


```python
from picozero import LED
from time import sleep

led = LED(14)

led.on()
sleep(1)
led.off()

```
---

## What’s Next?

In **Session 2 – Build**, you’ll:

* Mount the caster wheel and TT motors on the purple chassis.
* Learn why a motor controller (H‑bridge) is required.
* Spin a motor ON/OFF in code.

Save your LED script as `blink_led.py` on the Pico if you’d like to keep it for reference.

---

### Check‑Out

* Pico seated correctly ✔️  
* Thonny interpreter set ✔️  
* LED blink observed ✔️  

See you in Session 2!

