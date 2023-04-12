from dataclasses import dataclass

@dataclass
class Mountain:
    name:str
    elevation:int

k2 =  Mountain("k2",256148)
print(k2)
k2_str = str(k2) 
print(type(k2_str))
print(k2_str)