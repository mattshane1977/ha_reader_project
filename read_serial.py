import serial
import time

port = 'COM12'
baud = 115200

try:
    ser = serial.Serial(port, baud, timeout=0.1)
    print(f"Connected to {port} at {baud}")
    
    # Reset the chip via UART RTS
    print("Resetting chip...")
    ser.setDTR(False)
    ser.setRTS(True)
    time.sleep(0.1)
    ser.setRTS(False)
    time.sleep(0.5)
    
    start_time = time.time()
    while time.time() - start_time < 5:
        if ser.in_waiting > 0:
            line = ser.read(ser.in_waiting)
            try:
                # S3 Bootloader can be a mix of UTF8 and raw
                print(line.decode('utf-8', errors='replace'), end='')
            except Exception as e:
                print(f"Error decoding: {e}")
    print("\nCapture finished.")
except Exception as e:
    print(f"Error: {e}")
finally:
    if 'ser' in locals() and ser.is_open:
        ser.close()
