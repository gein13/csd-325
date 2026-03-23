def bottles_song():
    try:
        bottles_of_booze = int(input("Enter number of bottles to start: "))
        
        if bottles_of_booze <= 0:
            print("You're out of beer? Go get some!")
            return
        
        while bottles_of_booze > 0:
            if bottles_of_booze > 1:
                print(f"{bottles_of_booze} bottles of beer on the wall, {bottles_of_booze} bottles of beer.")
                print(f"Take one down and pass it around, {bottles_of_booze - 1} {'bottle' if bottles_of_booze - 1 == 1 else 'bottles'} of beer on the wall.\n")
            else:
                print("1 bottle of beer on the wall, 1 bottle of beer.")
                print("Take one down and pass it around, no more bottles of beer on the wall.\n")
            
            bottles_of_booze -= 1

        print("Sad face. You're out of beer. Go buy more and start the countdown again!")
        

    except ValueError:
        print("Invalid input. Please enter a whole number.")

bottles_song()