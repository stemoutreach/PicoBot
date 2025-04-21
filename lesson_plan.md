# PicoBot Lesson Plan

A three‑session workshop for middle/high‑school coding clubs: students build and program their own **Raspberry Pi Pico WH‑powered robot** while learning MicroPython fundamentals, electronics, and basic robotics concepts.

## Session Overview

| # | Topic | Description |
|---|-------|-------------|
| 1 | [Getting Started](Session1_GettingStarted.md) | Flash MicroPython, configure Thonny, blink the onboard LED, and mount the Pico on a breadboard. |
| 2 | [Build & Motors](Session2_Build.md) | Attach caster + TT motors, learn why we need an H‑bridge, spin a motor, intro to PWM speed control. |
| 3 | [Finish Build & Python Basics](Session3_Finish.md) | Wire battery + motor controller, verify two‑motor drive, review variables, loops, conditionals, and write a figure‑8 routine. |

## Hardware Bill of Materials (per student)

* Raspberry Pi Pico WH
* Purple aluminum robot chassis
* 2 × TT 3‑6 V gear motors + brackets
* Caster bearing wheel
* Motor controller (L9110 or L298N)
* 2 × 18650 Li‑Ion battery pack (or 4 × AA) & switch
* Half‑size breadboard + jumper wires
* Raspberry Pi 500 keyboard‑computer + portable monitor (dev station)

## Software Requirements

* Raspberry Pi OS (Bookworm 64‑bit) on the Pi 500
* Thonny IDE 4.x with **MicroPython (Raspberry Pi Pico)** interpreter selected
* `pico-utils` package (`sudo apt install pico-utils`) – provides `picotool` for troubleshooting (optional)

## Repo Layout

```
./
├── Session1_GettingStarted.md
├── Session2_Build.md
├── Session3_Finish.md
└── docs/
    └── img/  (diagrams & photos)
```

> **Tip:** Each session ends with a checklist so students and instructors can track progress.

Enjoy building your fleet of PicoBots and feel free to open issues or pull requests with improvements!

