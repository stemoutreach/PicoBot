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
| TT DC 3–6 V gear motor and Tire | 2 |
| Pi 500 + Pico on breadboard | 1 |
| Purple aluminium chassis | 1 |
| Caster bearing wheel + screws | 1 set |
| Motor mounting hardware | 2 sets |
| Screwdriver | 1 |

> **Safety note:** Drive the motor only in 0.5 s bursts to avoid overloading the Pico.

---

## 1 · Motor Polarity Demo (15 min)

### Demo Powering One Motor 

### Reverse by Swapping Leads

**Discuss:** Why can’t we keep driving motors directly from GPIO? → current limits, only one direction, no speed control.

---

## 2 · Mechanical Assembly (25 min)

1. **Motor brackets** – Align each TT motor shaft forward; mount with screws.

    <img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/PicoBot01.jpg" width="600" > 
    
    <img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/PicoBot02.jpg" width="600" > 
    
    <img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/PicoBot03.jpg" width="600" > 
    
    <img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/PicoBot04.jpg" width="600" > 
    
    <img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/PicoBot05.jpg" width="600" > 
    




2. **Caster** – Secure to the front of the chassis.


    <img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/PicoBot07.jpg" width="600" > 
    
    <img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/PicoBot08.jpg" width="600" > 
    
    <img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/PicoBot09.jpg" width="600" > 


4. Route motor leads into the chassis cut‑out toward the breadboard.
   
    <img src="https://github.com/stemoutreach/PicoBot/blob/main/zzimages/PicoBot06.jpg" width="600" > 

*(Demonstrate proper orientation before students tighten screws.)*


## 4 · Wrap‑Up & Teaser for Session 3 (5 min)

* Forward & reverse observed via lead swap ✔️  
* Caster + both motors mounted ✔️  
* Students articulate need for motor controller ✔️  

**Next session:** introduce the motor controller (H‑bridge), add battery power, and code driven reversal + speed control.

