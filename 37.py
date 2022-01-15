#Exs 37

V1 = int(input("Enter speed of Car1 per hour:"))
V2 = int(input("Enter speed of Car2 per hour:"))
t = int(input("Enter minutes:"))
S_distance_cars = int(input("Enter current distance between cars in kilometers:"))
V1_speed_minutes = V1/60
V2_speed_minutes = V2/60
S_new = (V1_speed_minutes * t) + (V2_speed_minutes * t) 
S = S_distance_cars - S_new
print("Old distance between cars:", S_distance_cars)
print("Distance gone by cars:", S_new)
print("Current Distance is:", S)