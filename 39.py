import math

A = int(input("Enter A:"))
B = int(input("Enter B:"))
C = int(input("Enter C:"))

D = math.pow(B,2) - 4 * A * C
# X1 = (-B + math.sqrt(D))/(2*A)
# X2 = (-B - math.sqrt(D))/(2*A)
# X0 = (-B/(2*A))
if D>0:
    X1 = (-B + math.sqrt(D))/(2*A)
    X2 = (-B - math.sqrt(D))/(2*A)
    print("D is:", D)
    print("X1 is:", X1)
    print("X2 is:", X2)
elif D==0: 
    X0 = (-B/(2*A))
    print("D is:", D)
    print("X0 is:", X0)
else: 
    print("No roots")