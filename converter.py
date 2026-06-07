while True:
    print("what would you like to convert?")
    print("\n1. Miles to Kilometers")
    print("2. Kilometers to Miles")
    print("3. Gallons to Liters")  # convert US gallons to Liters
    print("4. Liters to Gallons ")

    choice = input("choose an opion: ")

    if choice == "1":
        miles = float(input("How many Miles do you want to convert?"))
        print("Kilometers:", round(miles * 1.60934, 3))
    elif choice == "2":
        km = float(input("How many Kilometers do you want to convert?"))
        print("Mailes:", round(km / 1.60934, 3))
    elif choice == "3":
        gallons = float(input("How many Gallons do you want to convert?"))
        print("Liters:", round(gallons * 3.78541, 3))
    elif choice == "4":
        liters = float(input("How many Liters do you want to convert?"))
        print("Gallons:", round(liters / 3.78541, 3))
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option")
