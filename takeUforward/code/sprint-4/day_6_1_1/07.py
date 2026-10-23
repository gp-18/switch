# Q7. Smart Thermostat Temperature Limiter (Practice - Encapsulation)
#
# Task:
# Design a `Thermostat` class that protects heating and cooling hardware by restricting user
# target temperatures to a safe operational envelope (10.0C <= temp <= 35.0C).
#
# Attributes:
# - device_id (str) : Thermostat hardware ID (public).
# - mode (str) : Operational mode: "OFF", "HEAT", or "COOL" (public).
# - __current_temp (float) : Current ambient temperature reading from sensor (private).
# - __target_temp (float) : Desired temperature (private).
#
# Methods:
# - __init__(self, device_id: str, ambient_temp: float):
#     Sets __current_temp and initializes __target_temp = 21.0.
# - set_target_temp(self, temp: float):
#     Validates that 10.0 <= temp <= 35.0. If valid, updates __target_temp.
#     Otherwise prints "Temperature out of safe bounds (10.0C - 35.0C).".
# - get_target_temp(self) -> float:
#     Returns __target_temp.
# - update_sensor(self, sensor_temp: float):
#     Updates __current_temp from hardware sensor reading.
# - get_status(self) -> str:
#     Returns "Device: {device_id} | Mode: {mode} | Current: {current_temp}C | Target: {target_temp}C".
#
# Example 1:
# Input:
# t = Thermostat("NEST-001", 18.5)
# t.mode = "HEAT"
# t.set_target_temp(23.5)
# t.set_target_temp(45.0)  # Extreme temperature rejected
# print(t.get_status())
# Output:
# Temperature out of safe bounds (10.0C - 35.0C).
# Device: NEST-001 | Mode: HEAT | Current: 18.5C | Target: 23.5C
#
# Example 2:
# Input:
# t = Thermostat("NEST-002", 25.0)
# t.update_sensor(26.2)
# print(t.get_target_temp())
# Output:
# 21.0
#
# Example 3 (Edge Case):
# Input:
# t = Thermostat("NEST-003", 15.0)
# t.set_target_temp(5.0)   # Too cold (< 10.0)
# print("Target temp remains:", t.get_target_temp())
# Output:
# Temperature out of safe bounds (10.0C - 35.0C).
# Target temp remains: 21.0
#
# Think About:
# - Encapsulating `__target_temp` prevents dangerous hardware extremes (freezing pipes / burning coils).
# - The sensor reading `__current_temp` is only updated via sensor callbacks, preventing external tampering.
# - Time Complexity: O(1) for all calls.
# - Space Complexity: O(1) auxiliary space.

# Write your Thermostat class below:

class Thermostat:
    def __init__(self, device_id: str, ambient_temp: float):
        # Write your code here
        pass

    def set_target_temp(self, temp: float):
        # Write your code here
        pass

    def get_target_temp(self) -> float:
        # Write your code here
        pass

    def update_sensor(self, sensor_temp: float):
        # Write your code here
        pass

    def get_status(self) -> str:
        # Write your code here
        pass
