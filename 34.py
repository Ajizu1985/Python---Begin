#Exs 34

kg = float(input("Pls enter kg = "))
price_choc_kg = int(input("Pls enter price per kg of chocolate = "))
price_candy_kg = int(input("Pls enter price per kg of candy= "))
price_chocolate = kg*price_choc_kg
price_candy = kg * price_candy_kg
diff_chocolate = price_chocolate - price_candy
diff_candy = price_candy - price_chocolate
if price_chocolate > price_candy:
        print(f"{kg} kg chocolage is expensive for {diff_chocolate} UZS")
else:
        print(f"{kg} kg candy is expensive for {diff_candy} UZS")