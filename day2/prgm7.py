'''
Write a program to accept percentage from the user and display the grade according to the following criteria:

         Marks                                    Grade
         > 90                                      A
         > 80 and <= 90                            B
         >= 60 and <= 80                           C
         below 60                                  D
'''

percentage = int(input("Enter the total mark percentage(%): "))

print("Grade: ", end="")
if percentage >= 90:
    print("A")
elif percentage >= 80:
    print("B")
elif percentage >= 60:
    print("C")
else:
    print("D")


