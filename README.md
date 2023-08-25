# GPS Tracking System

![Project Image](project_image.jpg)

## Overview

This project involves creating a GPS tracking device using LoRa, Bluetooth, and GPS modules with an STM32 microcontroller. The device reads and processes GPS data, transmits it over LoRa to a receiving device, and also sends the data to a computer over Bluetooth. A Python application is used to display real-time GPS data on a map.

## Components

- STM32 Microcontroller (Transmitter)
- STM32 Microcontroller (Receiver)
- LoRa Module
- Bluetooth Module
- GPS Module
- Computer (Receiver)

## Transmitter Code

The transmitter code (STM32 microcontroller) reads GPS data from the GPS module, processes it, and transmits it to a receiving device using LoRa communication. Relevant code files include `main.c` and `lwgps/lwgps.h`. Key functions include:

- Initializing UART for GPS, LoRa, and Bluetooth communication.
- Processing GPS data using the lwGPS library.
- Transmitting GPS data over LoRa when a sufficient number of satellites are in view.

## Receiver Code

The receiver code (STM32 microcontroller) receives GPS data transmitted over LoRa from the transmitter and sends this data to a computer over Bluetooth. The relevant code file is `main.c`. Key functions include:

- Initializing UART for LoRa and Bluetooth communication.
- Receiving GPS data transmitted over LoRa.
- Sending GPS data to a computer over Bluetooth.

## Computer Application

The computer application written in Python connects to the receiving device over Bluetooth, reads the received GPS data, and displays it on a map using the TkinterMapview library. The Python script file is `gps_tracker.py`. Key functions include:

- Establishing a Bluetooth connection with the receiver device.
- Reading and parsing GPS data received over Bluetooth.
- Displaying real-time GPS data on a map using TkinterMapview.

## Usage

1. Load the transmitter and receiver STM32 microcontrollers with their respective code.
2. Connect the LoRa, Bluetooth, and GPS modules to the microcontrollers.
3. Run the computer application (`gps_tracker.py`) on your computer.
4. Ensure that both transmitter and receiver devices are powered on and within communication range.
5. GPS data is transmitted from the transmitter to the receiver via LoRa.
6. The receiver sends the GPS data to the computer over Bluetooth.
7. The computer application displays real-time GPS data on a map.

## Dependencies

- lwGPS Library (For processing GPS data on the transmitter device)
- TkinterMapview Library (For displaying GPS data on the computer)

## Note

- Ensure that the COM port in the computer application matches the Bluetooth COM port.
- Double-check the UART communication settings (baud rate, data bits, parity, stop bits) are configured correctly in both transmitter and receiver code.
