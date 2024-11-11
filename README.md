# Drone Controller

A Python script designed to automatically detect and connect to a nearby drone and safely initiate a shutdown sequence. This script includes a simple terminal animation and outputs in red for added effect.

## Features

- Automatically scans and connects to available drones.
- Initiates safe shutdown, attempting to land the drone. If landing fails, it triggers an emergency disarm.
- Simple animated console output and red text display for dramatic effect.

## Requirements

- **Python 3.6+**
- **dronekit** library
- **pymavlink** library

You can install the dependencies using:

```bash
pip install dronekit pymavlink
