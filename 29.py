#Exs 29

from math import*


while True:
        Alfa = int(input("Pls enter degree of an angle = "))
        if Alfa > 0 and Alfa < 360:
                Rad = Alfa * pi/180
                print(f"{Alfa} degree in radians is: {Rad}")
                break
        else:
                print("Pls enter an angle between 0 and 360")