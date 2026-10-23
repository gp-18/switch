# Q8. Tamper-Proof Car Odometer & Dashboard (Practice - Encapsulation)
#
# Task:
# Design a `CarDashboard` class. In real vehicles, the odometer can never be rolled back
# (it must be strictly monotonic), and speed must never exceed vehicle physical limits or drop below zero.
#
# Attributes:
# - vin (str) : Vehicle Identification Number (public).
# - model (str) : Car model name (public).
# - __odometer_km (float) : Cumulative distance traveled (private).
# - __speed_kmh (float) : Current vehicle speed (private).
# - __max_speed (float) : Top speed limit for this model (private).
#
# Methods:
# - __init__(self, vin: str, model: str, max_speed: float):
#     Initializes odometer to 0.0, speed to 0.0, and max speed to max_speed.
# - accelerate(self, amount: float):
#     Increases speed by amount (if amount > 0), capping at __max_speed.
# - brake(self, amount: float):
#     Decreases speed by amount (if amount > 0), floored at 0.0.
# - drive(self, distance_km: float):
#     If distance_km > 0, increases __odometer_km by distance_km.
#     If distance_km <= 0, prints "Invalid travel distance.".
# - get_odometer(self) -> float:
#     Returns total kilometers recorded.
# - get_speed(self) -> float:
#     Returns current vehicle speed.
#
# Example 1:
# Input:
# car = CarDashboard("1HGCR2F83HA", "Sedan GT", 220.0)
# car.accelerate(50.0)
# car.accelerate(200.0)  # Should cap at max_speed (220.0)
# print("Speed:", car.get_speed())
# car.brake(100.0)
# print("Braked Speed:", car.get_speed())
# car.drive(150.5)
# car.drive(-20.0)       # Tampering attempt (odometer roll-back)
# print("Odometer Reading:", car.get_odometer())
# Output:
# Speed: 220.0
# Braked Speed: 120.0
# Invalid travel distance.
# Odometer Reading: 150.5
#
# Example 2:
# Input:
# car = CarDashboard("2T1BR32EX1C", "Eco Hatch", 180.0)
# car.accelerate(80.0)
# car.brake(90.0)       # Braking beyond 0 floors at 0.0
# print("Floored Speed:", car.get_speed())
# Output:
# Floored Speed: 0.0
#
# Example 3 (Edge Case):
# Input:
# car = CarDashboard("3VWDP7AJ3FM", "Truck XL", 160.0)
# car.accelerate(-30.0)  # Negative acceleration ignored
# car.drive(0.0)         # 0 distance rejected
# print("Speed:", car.get_speed())
# print("Odometer:", car.get_odometer())
# Output:
# Invalid travel distance.
# Speed: 0.0
# Odometer: 0.0
#
# Think About:
# - Odometer Monotonicity: Hiding `__odometer_km` ensures mileage cannot be decreased.
# - Speed bounds [0, max_speed] are strictly maintained internally.
# - Time Complexity: O(1) for all updates.
# - Space Complexity: O(1) auxiliary space.

# Write your CarDashboard class below:

class CarDashboard:
    def __init__(self, vin: str, model: str, max_speed: float):
        # Write your code here
        pass

    def accelerate(self, amount: float):
        # Write your code here
        pass

    def brake(self, amount: float):
        # Write your code here
        pass

    def drive(self, distance_km: float):
        # Write your code here
        pass

    def get_odometer(self) -> float:
        # Write your code here
        pass

    def get_speed(self) -> float:
        # Write your code here
        pass
