'''
Write a program to calculate the electricity bill (accept number of unit from user) according to the following criteria :
           Unit                                                       Price  
      First 100 units                                               no charge
      Next 100 units                                              Rs 5 per unit
      After 200 units                                             Rs 10 per unit
'''

units = float(input("Enter unit(s) used: "))
charge = 0
if units > 200:
    charge = (units - 200) * 10 + 500
elif units > 100:
    charge = (units - 100) * 5
print(f"Bill amount for {units} unit(s): {charge}")
