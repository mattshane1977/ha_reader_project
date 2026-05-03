import machine
import neopixel
import time

# Pin 48 is common for RGB LED on ESP32-S3 DevKits
led_pin = 48
n = 1 # Number of pixels

np = neopixel.NeoPixel(machine.Pin(led_pin), n)

print(f"Blinking RGB LED on Pin {led_pin}...")

colors = [
    (255, 0, 0),   # Red
    (0, 255, 0),   # Green
    (0, 0, 255),   # Blue
    (255, 255, 255) # White
]

while True:
    for color in colors:
        print(f"Setting color to {color}")
        np[0] = color
        np.write()
        time.sleep(0.5)
        np[0] = (0, 0, 0)
        np.write()
        time.sleep(0.5)

