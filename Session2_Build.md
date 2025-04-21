# Session 2 – Chassis Assembly & Motor Polarity Demo

**Goal:** Bolt the caster wheel and two TT gear motors onto the chassis, then _manually_ power one motor to observe how wire polarity controls direction. Students should leave asking: “How could we do reversal in code?” (Answer comes with the motor controller in Session 3.)

---

## Learning Objectives

* Mechanical assembly of caster and motors.
* Observe DC motor behaviour with direct battery power.
* Understand that reversing voltage polarity reverses rotation.
* Preview the need for a motor controller (no wiring yet).

---

## Materials

| Item | Qty |
|------|-----|
| Purple aluminium chassis | 1 |
| Caster bearing wheel + screws | 1 set |
| TT DC 3–6 V gear motor | 2 |
| Motor mounting brackets & hardware | 2 sets |
| 2 × AA battery holder (3 V) or bench power supply with clip leads | 1 |
| Multimeter (shared) | – |
| Screwdriver | 1 |

> **Why no motor controller today?** We want students to physically swap the wires and _see_ polarity ≙ direction before abstracting it to code. The controller (H‑bridge) arrives in Session 3.

---

## 1 · Mechanical Assembly (30 min)

1. **Caster first** – Mount on the single‑hole end of the chassis using M3 screws & nuts.
2. **Motor brackets** – Align each TT motor so its shaft faces forward through the big side cut‑outs. Secure with two screws each.
3. _Do not_ wire anything yet—just leave the red/black motor leads hanging out the top for testing.

*(Hold up an example build so students match orientation.)*

---

## 2 · Motor Polarity Experiment (20 min)

1. Clip or hold the **battery pack leads** to one motor’s red/black wires (red→red, black→black). The wheel turns **forward**.
2. Swap the battery leads (red→black, black→red). The wheel now spins **reverse**.
3. Ask students: **“How could we swap polarity _electronically_ instead of physically?”** – collect ideas; introduce the term **H‑bridge** but save details for Session 3.

Optional: use a **multimeter in DC amps mode** to show that the motor draws far more current than a Pico GPIO pin can supply.

---

## 3 · Optional Stretch – PWM Concept with LED (10 min)

Even though we’re not yet driving motors from code, we can demo PWM speed control idea using the Pico’s LED:

```python
import machine, time
led = machine.PWM(machine.Pin("LED"))
led.freq(1000)
for duty in (1000, 10000, 30000, 50000):
    led.duty_u16(duty)
    time.sleep(1)
led.deinit()
```

Students see brightness scale and link that to motor speed.

---

## 4 · Wrap‑Up & Teaser for Session 3 (5 min)

* Caster & both motors mounted ✔️  
* Forward vs. reverse demonstrated by swapping wires ✔️  
* Students articulate need for electronic polarity switch ✔️  

**Next session:** add the motor controller (H‑bridge), wire batteries properly, and write Python to drive both motors in code.

