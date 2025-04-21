# Session 2 – Chassis Assembly & Motor Polarity Demo

**Goal:** Attach caster wheel and TT motors, then briefly power a motor from a Pico GPIO pin to observe one‑direction motion. Students swap the motor wires to see reversal and realise why a dedicated motor controller is essential.

---

## Learning Objectives

* Complete mechanical assembly of caster + motors.
* Safely power a TT motor *momentarily* from the Pico’s 3 V GPIO to observe rotation.
* Discover that swapping the motor leads flips direction.
* Understand limitations of powering motors directly from the Pico.

---

## Materials

| Item | Qty |
|------|-----|
| Purple aluminium chassis | 1 |
| Caster bearing wheel + screws | 1 set |
| TT DC 3–6 V gear motor | 2 |
| Motor mounting brackets & hardware | 2 sets |
| Male–female jumper wires | 2 |
| Pi 500 + Pico on breadboard | 1 |
| Multimeter (shared) | – |

> **Safety note:** A Pico GPIO can source ~15 mA—just enough to spin an unloaded TT motor for a second or two. We’ll run *short bursts only* (< 1 s) to avoid brown‑outs. Real operation will use a motor controller in Session 3.

---

## 1 · Mechanical Assembly (25 min)

1. **Caster first** – Secure on the single‑hole end of the chassis.  
2. **Motor brackets** – Align shafts forward; attach motors with two screws each.  
3. Route motor leads to the breadboard area.

---

## 2 · Wire One Motor for Momentary Test (10 min)

| Motor lead | Pico pin |
|------------|----------|
| **Red** | **GPIO 15** (physical 20) |
| **Black** | **GND** (physical 38) |

Use jumper wires from the motor leads straight to the Pico header pins.

---

## 3 · Momentary Spin Code (10 min)

```python
import machine, time
MOTOR = machine.Pin(15, machine.Pin.OUT)

for _ in range(3):
    MOTOR.high()   # apply 3.3 V – motor spins
    time.sleep(0.5)
    MOTOR.low()    # stop; let voltage recover
    time.sleep(0.5)
```

Observe forward rotation. Keep bursts short—if the Pico resets, you’ve over‑loaded it.

---

## 4 · Reverse by Swapping Leads (10 min)

Unplug the Pico. Swap the red/black leads on the breadboard, rerun the script—the wheel now spins the opposite direction.

### Guided Discussion

* *“Why can’t we just leave the motor wired to a GPIO and use `.high()` / `.low()` forever?”*  
  → Current limits, brown‑out resets, inability to power two motors.  
* *“How could software reverse without swapping wires?”*  
  → Need an H‑bridge (motor controller) and separate 5 V battery rail.

---

## 5 · (Stretch) PWM Concept with LED (if time, 5 min)

Demonstrate varying duty cycle on the Pico LED to foreshadow speed control.

---

## 6 · Wrap‑Up & Teaser for Session 3 (5 min)

* Caster & both motors mounted ✔️  
* One motor observed forward & reverse via wire swap ✔️  
* Understood GPIO current limits ✔️  

**Next session:** introduce the motor controller (H‑bridge), wire battery power, and write code to drive both motors safely.

