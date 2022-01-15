#Exs 36

V1 = int(input("Enter speed of Car1 per hour:"))
V2 = int(input("Enter speed of Car2 per hour:"))
t = int(input("Enter minutes:"))
S_old = int(input("Enter current distance in meters:"))
V1_speed_minutes = V1/60
V2_speed_minutes = V2/60
S_new = (V1_speed_minutes * t) + (V2_speed_minutes * t) 
S = S_new + S_old
print("Old Distance is:", S_old)
print("New Distance is:", S_new)
print("Total Distance is:", S)