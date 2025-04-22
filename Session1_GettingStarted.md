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

## 1 · Place the Pico on the Breadboard

1. Orient the breadboard like the image below.  
2. Hold the Pico with the **USB port facing the top**.
3. The ower rails should be + - on both sides.
4. Align the two rows of header pins over the **center groove**.  
5. Make sure the component rails start with 1 at the top.
6. Press gently until all pins seat flush— Pico pin 1 should be in row 1 column c, pico pin 40 should be in column h.  

    <img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/PicoBreadboard.jpg" width="400" > 

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
import machine, time

# Built‑in LED alias works on Pico and Pico W/WH
led = machine.Pin("LED", machine.Pin.OUT)

for _ in range(5):
    led.toggle()
    time.sleep(0.3)
```

Press ▶️ Run. The small **green LED near the antenna** blinks five times.

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

