"""
Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
          Sample String : 'The quick Brow Fox'
          Expected Output :
          No. of Upper case characters : 3
          No. of Lower case Characters : 12
"""


def upper_lower_count(string):
    upper_count = 0
    lower_count = 0
    for i in string:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
    return {"upper_count": upper_count, "lower_count": lower_count}


string = "The quick Brow Fox"
result = upper_lower_count(string)
print("No. of Upper case characters:", result["upper_count"])
print("No. of Lpper case characters:", result["lower_count"])
