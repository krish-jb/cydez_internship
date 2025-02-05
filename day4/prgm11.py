# Reverse Dictionary mapping  ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
ascii_dict = {"A": 65, "B": 66, "C": 67, "D": 68} 
print({val: key for key, val in ascii_dict.items()})
