# Raspberry Pi 500 + Raspberry Pi Pico WH – Classroom Setup Guide

A concise, repeatable set of steps for preparing each **Raspberry Pi 500** workstation and **Raspberry Pi Pico WH** microcontroller for MicroPython development. Ideal for coding‑club or workshop use where every student builds and programs a personal PicoBot.

---

\## Prerequisites

| Item                             | Notes                                                                         |
| -------------------------------- | ----------------------------------------------------------------------------- |
| **Pi 500**                       | SD card pre‑imaged with Raspberry Pi OS (Bookworm 64‑bit).                    |
| **Portable monitor**             | Connected via **micro‑HDMI 0** (left‑hand port).                              |
| **USB mouse + power supply**     | Standard Pi 5 USB‑C power brick.                                              |
| **Raspberry Pi Pico WH**         | Pre‑flashed with MicroPython UF2 (optional if you want to practise flashing). |
| **USB‑A ↔ micro‑USB data cable** | One per student—must support data, not just charging.                         |
| **Internet (optional)**          | Only needed if you plan to update packages live.                              |

---

\## A · Prepare the Pi 500 Workstation

1. **Insert the SD card & cable up the desk**\
   • Slide the micro‑SD into the slot underside the keyboard.\
   • Connect the portable monitor, mouse, and USB‑C power.

2. **First‑boot wizard**\
   Complete locale, keyboard, and Wi‑Fi prompts. (Skip Wi‑Fi if offline.)

3. **Update packages** *(recommended)*

   ```bash
   sudo apt update && sudo apt full-upgrade -y
   ```

4. **Install Git & picotool** *(optional)*

   ```bash
   sudo apt install git gh picotool -y
   ```

5. **Launch Thonny & set interpreter**\
   *Menu ▸ Programming ▸ Thonny* → **Tools ▸ Options ▸ Interpreter** →\
   Select **MicroPython (Raspberry Pi Pico)** and leave *Port* on **Automatic**.

---

\## B · Prepare the Pico WH

> If the UF2 is already flashed you can skip Step 2.

1. **Plug in**\
   Connect the Pico’s micro‑USB to a USB‑A port on the Pi 500.

2. **Flash MicroPython UF2** *(only if needed)*

   1. Hold **BOOTSEL** on the Pico.
   2. While holding the button, plug in the USB cable. A new drive **RPI‑RP2** appears.
   3. Drag‑and‑drop the latest `pico_micropython_*.uf2` onto the drive. The Pico reboots automatically.

3. **Open the REPL in Thonny**\
   Click the green ▶️ Run button (or press **Ctrl‑D**) and look for `>>>` prompt.

4. **Quick sanity test**

   ```python
   import machine, time
   led = machine.Pin(25, machine.Pin.OUT)
   for _ in range(5):
       led.toggle()
       time.sleep(0.3)
   ```

   The on‑board LED should blink.

5. **Save a script to run at boot**\
   *File ▸ Save As ▸ Raspberry Pi Pico* → name it `main.py`. Anything named `main.py` auto‑runs on power‑up.

6. **Eject cleanly**\
   In Thonny choose *Run ▸ Stop/Restart backend* before unplugging USB.

---

\## Troubleshooting Quick Ref

| Symptom                               | Likely Cause & Fix                                                                                                                       |                          |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------- | ------------------------ |
| **Thonny: “device busy / no access”** | • Pico still in BOOTSEL mode — unplug & re‑plug without button.• Using a charge‑only cable — swap for data‑capable cable.• Check \`dmesg | tail`for`/dev/ttyACM0\`. |
| **Nothing after flashing UF2**        | Unplug → re‑plug; firmware finishes reboot cycle.                                                                                        |                          |
| **Need factory reset**                | Hold **BOOTSEL** while powering the Pico to re‑enter mass‑storage mode and copy a fresh UF2.                                             |                          |

---

\## Desk‑Side Checklist (laminate & tape down)

1. Power Pi 500 → login.
2. Open Thonny → Interpreter = *MicroPython (Pico)*.
3. Plug Pico WH → REPL appears.
4. Run LED blink test → success ✔️.
5. Code → save `main.py` → `git add . && git commit -m "Lab‑1"`.

Enjoy your PicoBot build!

