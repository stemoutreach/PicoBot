from picozero import LED
from time import sleep

led = LED(14)

led.on()
sleep(1)
led.off()
