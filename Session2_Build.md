# Session 2 – Motor Polarity Demo **Before** Mechanical Assembly

**Goal:** Powered by a Pico GPIO pin, students spin a TT motor _before_ it’s mounted, physically swap leads to reverse direction, then bolt both motors and the caster to the chassis. This order lets them understand polarity *before* hiding wires inside the frame.

---

## Learning Objectives

* Observe a DC motor spinning forward and reverse by swapping leads.
* Recognise GPIO current limits → need for motor controller later.
* Complete chassis assembly after the demo.

---

## Materials

| Item | Qty |
|------|-----|
| TT DC 3–6 V gear motor | 2 |
| Male–female jumper wires | 2 |
| Pi 500 + Pico on breadboard | 1 |
| Multimeter (shared) | – |
| Purple aluminium chassis | 1 |
| Caster bearing wheel + screws | 1 set |
| Motor mounting brackets & hardware | 2 sets |
| Screwdriver | 1 |

> **Safety note:** Drive the motor only in 0.5 s bursts to avoid overloading the Pico.

---

## 1 · Bench‑Top Motor Polarity Demo (15 min)

### Wire One Motor Temporarily

| Motor lead | Pico pin |
|------------|----------|
| **Red** | **GPIO 15** (physical 20) |
| **Black** | **GND** (physical 38) |

### Code to Spin Forward

```python
import machine, time
MOTOR = machine.Pin(15, machine.Pin.OUT)
for _ in range(3):
    MOTOR.high()   # 3.3 V forward
    time.sleep(0.5)
    MOTOR.low()    # coast/stop
    time.sleep(0.5)
```

### Reverse by Swapping Leads

Unplug USB, swap red/black jumpers at the Pico header, re‑run script. Motor spins opposite direction.

**Discuss:** Why can’t we keep driving motors directly from GPIO? → current limits, only one direction, no speed control.

---

## 2 · Mechanical Assembly (25 min)

1. **Caster first** – Secure to the single‑hole end of the chassis.  
2. **Motor brackets** – Align each TT motor shaft forward; mount with screws.  
3. Route motor leads into the chassis cut‑out toward the breadboard.

*(Demonstrate proper orientation before students tighten screws.)*

---

## 3 · Optional Stretch – PWM Concept with LED (5 min)

```python
import machine, time
led = machine.PWM(machine.Pin("LED"))
led.freq(1000)
for duty in (2000, 10000, 30000, 50000):
    led.duty_u16(duty)
    time.sleep(1)
led.deinit()
```

Brightness levels hint at motor speed control coming up.

---

## 4 · Wrap‑Up & Teaser for Session 3 (5 min)

* Forward & reverse observed via lead swap ✔️  
* Caster + both motors mounted ✔️  
* Students articulate need for motor controller ✔️  

**Next session:** introduce the motor controller (H‑bridge), add battery power, and code driven reversal + speed control.

