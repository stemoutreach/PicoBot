# Session 3 – Finish Build & Python Basics

**Goal:** Complete electrical wiring (battery + motor controller), verify two‑motor drive, and reinforce core Python constructs.

---

## Learning Objectives

* Safely power the robot with batteries.
* Drive both motors forward, reverse, and stop.
* Review Python: variables, loops, conditionals, functions.

---

## Materials

| Item | Qty |
|------|-----|
| Assembled chassis with motors | 1 |
| Motor controller board (L9110/L298N) | 1 |
| 2× 18650 Li‑Ion battery pack (or 4× AA) | 1 |
| Barrel‑jack or JST‑PH pigtail | 1 |
| Multimeter (shared) | – |
| Pi 500 + Pico on breadboard | 1 |

---

## 1 · Wire Battery to Motor Controller (15 min)

1. **Polarity check** – Use multimeter; red = + V, black = GND.  
2. Connect battery **+** to `VCC` (or `VIN`) and battery **–** to `GND` on the driver.  
3. Do *not* tie battery + to Pico 5 V; the driver’s `5V OUT` pin powers logic if needed.

> **Safety tip:** Add an inline power switch or pull the battery when not testing.

---

## 2 · Dual‑Motor Drive Test (15 min)

Extend the code from Session 2:

```python
import machine, time
IN1, IN2, IN3, IN4 = (machine.Pin(p, machine.Pin.OUT) for p in (2, 3, 6, 7))

def drive(left_fwd, left_rev, right_fwd, right_rev, t=1):
    IN1.value(left_fwd)
    IN2.value(left_rev)
    IN3.value(right_fwd)
    IN4.value(right_rev)
    time.sleep(t)
    IN1.low(); IN2.low(); IN3.low(); IN4.low()

# Forward 1 s
drive(1,0, 1,0, 1)
# Reverse 1 s
drive(0,1, 0,1, 1)
```

Robot should roll forward, pause, then reverse.

---

## 3 · Python Basics Refresher (20 min)

| Concept | Mini Exercise |
|---------|--------------|
| **Variables** | Store `speed = 50000` and reuse in PWM duty cycle. |
| **Loops** | `for _ in range(4):` drive square pattern. |
| **Conditionals** | `if left_speed > right_speed:` print turn direction. |
| **Functions** | Wrap motion blocks: `def forward(t, duty): ...` |

**Group challenge:** Write a function `figure_eight()` that calls `forward`, `pivot_left`, and `pivot_right` to trace a figure 8 on the floor.

---

## 4 · Checklist & Next Steps (10 min)

* Battery safely attached ✔️  
* Both motors respond to code ✔️  
* Python constructs practised ✔️  

### Stretch Goals

* Add PWM speed control to `forward()` and `reverse()`.
* Mount ultrasonic sensor and write `avoid_obstacle()`.

---

Great job—your PicoBot is now mobile **and** you’ve brushed up on essential Python skills. Feel free to keep experimenting and share your figure‑8 videos in the class repo!

