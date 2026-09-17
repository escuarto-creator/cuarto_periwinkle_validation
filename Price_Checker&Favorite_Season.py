#item price validator
try:
    input_price = float(input("Enter the item price: "))
    if input_price <= 0:
        print("Invalid price. Please enter a positive value.")
    else:
        print(f"The price entered is {input_price}.")
except ValueError:
    print("Invalid input. Please enter a valid number.")


#Favorite season checker
allowed_seasons = ["spring", "summer", "fall", "winter", "Spring", "Summer", "Fall", "Winter", "SPRING", "SUMMER", "FALL", "WINTER"]
favorite_season = input("Enter your favorite season: ")
if favorite_season in allowed_seasons:
    print(f"Your favorite season is {favorite_season}.")
else:
    print("Invalid season entered. Please choose from spring, summer, fall, or winter.")