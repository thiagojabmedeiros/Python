dict = {}
dict["brazil"] = 1 # O(1)
dict["chile"] = 2 # O(1)
dict["japan"] = 3 # O(1)
print(dict)
print(dict.get("brazil", 0)) # O(1)
print(dict.get("usa", 0)) # O(1)
dict["brazil"] = dict.get("brazil", 0) + 1
print(dict)
dict["usa"] = 4
print(dict)
dict.pop("usa") # O(1)
print(dict.pop("brazil")) # O(1) - this pop function remove the pair k&v by k and returns the v
print(dict)