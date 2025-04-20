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

4. **Install Git & Pico utilities (includes `picotool`)**  
   ```bash
   sudo apt update
   sudo apt install git gh pico-utils -y   # installs picotool, elf2uf2, etc.
   ```  
   <details><summary><em>Package not found?</em></summary>
   
   Enable the official Raspberry Pi repository, then retry:
   
   ```bash
   echo "deb http://archive.raspberrypi.org/debian $(lsb_release -sc) main" | \
        sudo tee /etc/apt/sources.list.d/raspi.list
   sudo apt update
   sudo apt install pico-utils -y
   ```
   
   If you still prefer building from source, see **Appendix A – Building `picotool` from source** at the end of this file.
   </details>
```bash
   sudo apt install git gh pico-utils -y  # "pico-utils" package contains picotool
   ```

5. **Launch Thonny & set interpreter**\
   *Menu ▸ Programming ▸ Thonny* → **Tools ▸ Options ▸ Interpreter** →\
   Select **MicroPython (Raspberry Pi Pico)** and leave *Port* on **Automatic**.

---

\## B · Prepare the Pico WH

> If the UF2 is already flashed you can skip Steps 2–3.

1. **Plug in**  <br>
   Connect the Pico’s micro‑USB to a USB‑A port on the Pi 500 (no buttons pressed).

2. **Download the latest MicroPython UF2** *(only required once; keep the file in Downloads)*  <br>
   1. On the Pi 500 open a browser and open **<https://www.raspberrypi.com/documentation/microcontrollers/micropython.html>** (or the short link **rpf.io/picow‑uf2**). This page lists both *Raspberry Pi Pico* and *Raspberry Pi Pico W* firmware builds.  <br>
   2. Scroll to the *MicroPython* section and click the newest file named like `pico‑<date>‑micropython.uf2`.  <br>
   3. Verify the file appears in **~/Downloads**.

3. **Flash MicroPython UF2** *(skip if already flashed)*  <br>
   1. Unplug the Pico.  <br>
   2. Hold **BOOTSEL**, then plug the Pico back in; a drive named **RPI‑RP2** mounts.  <br>
   3. Drag‑and‑drop the UF2 from `~/Downloads` onto the drive. The Pico reboots automatically when the copy finishes.

4. **Open the REPL in Thonny**  <br>
   Click the green ▶️ Run button (or press **Ctrl‑D**) and look for the `>>>` prompt.

5. **Quick sanity test**  <br>
   ```python
   import machine, time
   led = machine.Pin("LED", machine.Pin.OUT)  # built‑in LED (GPIO 25 on Pico, GPIO 0 on Pico W/WH)
for _ in range(5):
    led.toggle()
    time.sleep(0.3)
```
   The on‑board LED should blink.

6. **Save a script to run at boot**  <br>
   *File ▸ Save As ▸ Raspberry Pi Pico* → name it `main.py`. Anything named `main.py` auto‑runs on power‑up.

7. **Eject cleanly**  <br>
   In Thonny choose *Run ▸ Stop/Restart backend* before unplugging USB.

## Troubleshooting Quick Ref Quick Ref

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

---

## Appendix A – Building `picotool` from source

Only necessary if `pico-utils` is unavailable on your image.

```bash
# Prerequisites
sudo apt install git cmake gcc-arm-none-eabi build-essential libusb-1.0-0-dev -y

# Clone source and the Pico SDK (as a submodule)
git clone --recursive https://github.com/raspberrypi/picotool
cd picotool

# Build
mkdir build && cd build
export PICO_SDK_PATH=$PWD/../pico-sdk   # CMake needs the SDK location
cmake ..
make -j$(nproc)

# Install globally
sudo make install
```

If you see **“Directory .../pico-sdk not found”**, ensure you cloned with `--recursive` or run:
```bash
git submodule update --init
```

