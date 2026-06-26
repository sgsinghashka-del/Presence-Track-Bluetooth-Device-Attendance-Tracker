from datetime import datetime
from bleak import BleakScanner
import asyncio

REGISTERED_DEVICES = {
    "x0:0x:x0:00:x0:0d": "Device name",

}
mark_today = set()

def detection_callback(device, advertisment_data):
    if device.name == TARGET_NAME:
        today = datetime.now().date()
        key = (TARGET_NAME, today)

        if key not in mark_today:
            mark_today.add(key)
            time_now = datetime.now().strftime("%H:%M:%S")
            print(f"✅ Attendance marked for {TARGET_NAME} at {time_now}")

async def scan_devices():
    print("📡 Scanning for Bluetooth devices...\n")
    scanner = BleakScanner(detection_callback=detection_callback)
    await scanner.start()
    await asyncio.sleep(30)
    await scanner.stop()
    print("\n🛑 Scan completed")

asyncio.run(scan_devices())
