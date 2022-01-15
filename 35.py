#Exs 35

while True:
        V = int(input("Enter boat speed:"))
        U = int(input("Enter river speed:"))
        if(V>U):
                hour = 1
                boat_speed = V / hour
                river_speed = U / hour
                boat_minutes_lake = 0.25 * hour
                boat_minutes_river = 0.25 * hour
                Distance_passed_lake = boat_minutes_lake * boat_speed 
                Distance_passed_river = boat_minutes_river * (boat_speed-river_speed) 
                
                print(f"The Boat passed {Distance_passed_lake} km in lake")
                print(f"The Boat passed {Distance_passed_river} km in river")
                break
        else: 
                print("Pls reconsider speed as the boat's speed is higher than the river's speed")