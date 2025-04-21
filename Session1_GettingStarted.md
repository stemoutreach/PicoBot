# Session 1 – Getting Started with the PicoBot

**Goal:** Every student plugs in their Raspberry Pi Pico WH, sees the onboard LED blink, and mounts the Pico correctly on the breadboard.

---

## Learning Objectives

* Flash & verify MicroPython on a Pico WH.
* Configure Thonny to talk to MicroPython.
* Run a first script that blinks the onboard LED.
* Place the Pico on the breadboard in a repeatable orientation.

---

## Materials

| Item | Qty (per student) |
|------|------------------|
| Raspberry Pi Pico WH | 1 |
| Breadboard (half‑size) | 1 |
| USB‑A ↔ micro‑USB data cable | 1 |
| Pi 500 workstation | 1 |

---

## 1 · Connect & Configure Thonny

1. **Plug the Pico in** (no BOOTSEL button).  
2. Open **Thonny** → *Tools ▸ Options ▸ Interpreter*.  
3. Set **Interpreter** = **MicroPython (Raspberry Pi Pico)**, **Port** = *Automatic* (or `/dev/ttyACM0`).  
4. Click **OK**. In the Shell you should see `>>>`.

> **Troubleshoot:** If you see the desktop prompt (`>>>` missing), check that the status bar says *MicroPython*. If not, re‑select the interpreter.

---

## 2 · Blink the On‑Board LED

```python
import machine, time

# Built‑in LED alias works on Pico and Pico W/WH
led = machine.Pin("LED", machine.Pin.OUT)

for _ in range(5):
    led.toggle()   # toggle ON/OFF
    time.sleep(0.3)
```

*Press ▶️ Run*. The small **green LED near the antenna** should flash five times.

---

## 3 · Place the Pico on the Breadboard

1. Orient the breadboard so the **blue minus (-) rail** is at the bottom.  
2. Insert the Pico **over the central groove** so **USB end points right**, antenna up.  
3. Ensure **row 1** of Pico pins goes into **column E** and **row 2** into **column F** (so each pin straddles the groove).  
4. Gently press until all headers are fully seated.

![breadboard orientation placeholder](docs/img/pico_breadboard_placement.png)

> *Tip:* Keep the Pico flush with the top edge of the breadboard—this leaves room for motor‑driver wiring at the bottom.

---

## 4 · What’s Next?

In **Session 2 – Build**, you’ll:

* Bolt the caster wheel and TT motors onto the purple chassis.
* Learn why a motor controller (H‑bridge) is required.
* Spin a motor ON/OFF and brainstorm reversing direction.

Save your LED script as `blink_led.py` on the Pico if you’d like to keep it as a reference.

---

### Check‑Out

* LED blink observed ✔️  
* Thonny interpreter set ✔️  
* Pico seated on breadboard ✔️  
* `blink_led.py` saved ✔️  

See you next session!

