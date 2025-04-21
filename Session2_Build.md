# Session 2 – Build & Intro to Motors

**Goal:** Attach the caster wheel and drive motors to the chassis, understand motor basics, and spin a motor from MicroPython.

---

## Learning Objectives

* Mechanical assembly: caster + two TT gear motors.
* Explain why direct‑to‑Pico motor power is dangerous.
* Illustrate H‑bridge concept and reversal of motor direction.
* Optional stretch: Explore PWM for speed control (LED or motor).

---

## Materials

| Item | Qty |
|------|-----|
| Purple aluminum chassis | 1 |
| Caster bearing wheel + screws | 1 set |
| TT DC 3–6 V gear motor | 2 |
| Mounting brackets & hardware | 2 sets |
| Screwdriver | 1 |
| Pi 500 + Pico on breadboard | 1 |

---

## 1 · Mechanical Assembly (30 min)

1. **Caster wheel first** – Mount it on the single‑hole side of the chassis using the supplied M3 screws and nuts.  
2. **Motor brackets** – Align each TT motor so the output shaft faces forward; attach with two M3×12 screws per bracket.  
3. Route motor wires **through the chassis slot** toward the breadboard area.

*(Hold up the finished example so students can match orientation.)*

---

## 2 · Motors 101 (10 min mini‑talk)

* Brushed DC motor anatomy: armature, brushes, magnets.  
* Voltage determines **speed**; reversing polarity flips direction.  
* **Problem:** The Pico can only source *~15 mA*; each motor needs +500 mA → **solution: motor controller**.

### Quick Q&A

> **Q:** “If direction depends on polarity, how do we swap polarity in software?”  
> **A:** Use an **H‑bridge** – four transistors that switch current paths.

Display H‑bridge diagram (projector or handout).

---

## 3 · Wire one motor via motor controller (15 min)

1. Connect **motor A** leads to **OUT1/OUT2** on the driver board.  
2. Wire **IN1/IN2** to Pico GPIO 2 and 3.  
3. Don’t connect motor power yet – we’ll add batteries in Session 3.

---

## 4 · First Spin! (15 min)

```python
import machine, time
IN1 = machine.Pin(2, machine.Pin.OUT)
IN2 = machine.Pin(3, machine.Pin.OUT)

def motor_forward():
    IN1.high(); IN2.low()

def motor_reverse():
    IN1.low(); IN2.high()

def motor_stop():
    IN1.low(); IN2.low()

motor_forward()
time.sleep(1)
motor_stop()
```

Ask students: *“How would you make it reverse?”* → implement `motor_reverse()`.

---

## 5 · Stretch Activity – PWM for Speed (if time)

```python
enable = machine.PWM(machine.Pin(4))  # ENA pin on driver
enable.freq(1000)                     # 1 kHz
for duty in (0, 20000, 40000, 60000):
    enable.duty_u16(duty)
    time.sleep(1)
```

Demo LED PWM first so students see brightness scaling.

---

## 6 · Wrap‑Up & Prep for Session 3

* Both motors solidly mounted ✔️  
* One motor spins forward & stops ✔️  
* Understand why we need an H‑bridge ✔️  

**Next time:** wire the motor controller to battery power, finish chassis build, and dive into Python basics (variables, loops, conditionals, functions).

