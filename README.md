📡 BlueAttend – Bluetooth-Based Attendance System in Python

BlueAttend is a Python-based automated attendance system that uses Bluetooth Low Energy (BLE) scanning to mark attendance when a specific device is detected nearby. The system continuously scans for nearby Bluetooth devices and automatically records attendance for a predefined target device, eliminating the need for manual check-ins.

This project is built using the Bleak library and Python’s asynchronous programming model, making it lightweight, efficient, and suitable for real-time proximity-based tracking.

✨ Key Features
Automatic attendance marking using Bluetooth device name detection
Prevents duplicate attendance entries for the same day
Real-time timestamp logging
Asynchronous scanning using asyncio
Console-based status updates for clarity


🛠️ Technologies Used
Python
Bleak (Bluetooth Low Energy scanning)
Asyncio
Datetime


📌 Use Cases
Classroom or training attendance systems
Office entry and presence tracking
IoT and proximity-based automation projects
Learning Bluetooth programming in Python



⚠️ Notes & Limitations
Requires Bluetooth-enabled hardware
Device name must be discoverable
Works best with BLE-supported devices
Some operating systems may require elevated permissions.
