
#Exs 30

from math import*

while True:
        Rad = float(input("Pls enter radians = "))
        if Rad > 0 and Rad < 2*pi:
                Alfa = (Rad*180)/pi
                print(f"{Rad} radians are {Alfa} in angle")
                break
        else:
                print(f"Pls enter radians below {2*pi}")