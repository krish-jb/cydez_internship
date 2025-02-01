# Create a child class Bus that will inherit all of the variables and methods of the Vehicle class

class Vechicle:
    def __init__(self, plate_no):
        self.plate_no = plate_no

class Bus(Vechicle):
    def __init__(self, name, plate_no):
        super().__init__(plate_no)
        self.category = "HMV"
        self.wheel_count = 4
        self.name = name
        
        
eve_maria = Bus("Eve Maria", "KL 32 L 3335")
print("Name:", eve_maria.name)
print("Plate No:", eve_maria.plate_no)
print("Category:", eve_maria.category)
print("Wheel Count:", eve_maria.wheel_count)
