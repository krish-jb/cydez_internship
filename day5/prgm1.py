class Animal:
    name = ""
    color = ""
    
    def __init__(self, name, color):
        self.name = name
        self.color = color
        
    def __str__(self):
        return f"The animal is a {self.name} and {self.color} in color."
        
        
cat = Animal("Cat", "White")
print(cat)