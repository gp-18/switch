# Cooperative Multiple Inheritance with **kwargs
# In multiple inheritance, different parent classes require different arguments.
# Implement cooperative constructor chaining using **kwargs:
#
# 1. Base:
#    - __init__(self, **kwargs): calls super().__init__()
#
# 2. NamedEntity(Base):
#    - __init__(self, name="Unknown", **kwargs):
#      sets self.name = name, and forwards remaining kwargs: super().__init__(**kwargs)
#
# 3. TimestampedEntity(Base):
#    - __init__(self, created_at=None, **kwargs):
#      sets self.created_at = created_at, and forwards remaining kwargs: super().__init__(**kwargs)
#
# 4. User(NamedEntity, TimestampedEntity):
#    - __init__(self, role="Member", **kwargs):
#      sets self.role = role, and forwards remaining kwargs: super().__init__(**kwargs)
#
# Example:
# Input:  u = User(name="Alice", created_at="2026-01-01", role="Admin")
# Output: u.name == "Alice", u.created_at == "2026-01-01", u.role == "Admin"
#
# Check that all arguments are properly extracted and no unexpected kwargs crash the call chain.
#

# Write your solution below:

class Base : 
    def __init__(self, **kwargs) :
        super().__init__()

class NamedEntity(Base) :
    def __init__(self , name = "Unknown" , **kwargs) :
        self.name = name 
        super().__init__(**kwargs)

class TimestampedEntity(Base) :
    def __init__(self , created_at = None , **kwargs) :
        self.created_at = created_at 
        super().__init__(**kwargs)

class User(NamedEntity , TimestampedEntity) :
    def __init__(self , role = "Member" , **kwargs) :
        self.role = role 
        super().__init__(**kwargs)

u = User(name="Alice", created_at="2026-01-01", role="Admin")
print(u.name, u.created_at, u.role)