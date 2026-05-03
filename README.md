# ESP32-S3 RFID Reader for Home Assistant

This project implements a high-performance RFID/NFC reader using an ESP32-S3 (16MB Flash, Octal PSRAM) and a PN532 NFC module. It integrates natively with Home Assistant's Tag system.

## Hardware Specifications
- **Microcontroller:** ESP32-S3 (DevKitC-1 variant)
- **Flash:** 16MB
- **PSRAM:** 8MB Octal (Mode: `qio_opi`, Speed: `40MHz`)
- **NFC Module:** PN532 (Connected via SPI)
- **Onboard LED:** RGB LED (GPIO 48)

## Pin Mappings

### PN532 (SPI)
| PN532 Pin | ESP32-S3 GPIO | Function |
|-----------|---------------|----------|
| SCK       | 12            | SPI Clock |
| MISO      | 13            | SPI MISO  |
| MOSI      | 11            | SPI MOSI  |
| NSS (CS)  | 10            | SPI Chip Select |

### RGB LED
| Function | ESP32-S3 GPIO |
|----------|---------------|
| Data     | 48            |

## Features
- **Home Assistant Integration:** Automatically reports scans to the Home Assistant "Tags" dashboard using `homeassistant.tag_scanned`.
- **Visual Feedback:** The onboard RGB LED turns green for 3 seconds upon a successful tag read.
- **Serial Debugging:** Configured for 115200 baud on UART0.

## Build and Installation

### Prerequisites
1. [ESPHome](https://esphome.io/guides/installing_esphome.html) installed locally.
2. A path without spaces in the directory names (to avoid PlatformIO build issues).

### Flashing
1. Clone this repository:
   ```bash
   git clone https://github.com/mattshane1977/ha_reader_project.git
   cd ha_reader_project
   ```
2. Update the `wifi` section in `reader-test.yaml` with your credentials.
3. Flash via USB (recommended for first time):
   ```bash
   esphome run reader-test.yaml --device COM11
   ```
   *(Replace `COM11` with your actual serial port)*

4. For future updates, OTA is enabled:
   ```bash
   esphome run reader-test.yaml --device 10.10.15.139
   ```

## Repository Contents
- `reader-test.yaml`: Primary ESPHome configuration.
- `esp32-s3-fixed.yaml`: Troubleshooting configuration for Octal PSRAM.
- `main.py`: MicroPython script for quick hardware validation.
- `read_serial.py`: Debugging script to capture boot logs.
