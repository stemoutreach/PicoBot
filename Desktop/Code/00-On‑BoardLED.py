import machine, time

# Built‑in LED alias works on Pico and Pico W/WH
led = machine.Pin("LED", machine.Pin.OUT)

for _ in range(5):
    led.toggle()
    time.sleep(0.3)