# Singleton Pattern via Controlled Construction (__new__ + __init__ Guard)
# Ensure only ONE instance of DatabaseConnection can ever exist.
#
# 1. DatabaseConnection:
#    - Maintain a class variable `_instance = None`.
#    - In __new__(cls, *args, **kwargs):
#      If _instance is None, create it via super().__new__(cls) and assign to _instance.
#      Return cls._instance.
#    - In __init__(self, db_name, host):
#      Notice that Python calls __init__ every time DatabaseConnection(...) is called!
#      Use a guard `if not hasattr(self, "_initialized"):` so initialization only runs ONCE
#      and later constructor calls do not overwrite existing state.
#      Set self._initialized = True.
#
# Example:
# Input:
#   db1 = DatabaseConnection("prod_db", "10.0.0.1")
#   db2 = DatabaseConnection("dev_db", "localhost")
# Output:
#   db1 is db2 == True
#   db2.db_name == "prod_db"
#   db2.host == "10.0.0.1"
#

# Write your solution below:

class DatabaseConnection:
    _instance = None

    def __new__(cls, *args, **kwargs):
        # Create the object only if it does not already exist.
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self, db_name, host):
        # Initialize the object only once.
        if not hasattr(self, "_initialized"):
            self.db_name = db_name
            self.host = host
            self._initialized = True


db1 = DatabaseConnection("prod_db", "10.0.0.1")
db2 = DatabaseConnection("dev_db", "localhost")

print(db1 is db2)
print(db2.db_name)
print(db2.host)