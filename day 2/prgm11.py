'''
Accept any city from the user and display monument of that city.
                  City                                 Monument
                  Delhi                               Red Fort
                  Agra                                Jal Mahal
                  Jaipur                              Taj Mahal
'''
city = input("Enter a city (Delhi, Agra, Jaipur): ").lower()
if "delhi" == city:
    print("Red Fort")
elif "agra" == city:
    print("Taj Mahal")
elif "jaipur" == city:
    print("Amar Jawan Jyoti")
else:
    print("Invalid input")

