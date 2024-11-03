
while True:
    key = input("Press '1' to continue or Press '0' to exit!..")
    
    try:
        if int(key) == 0:
            print("Zero pressed...")
            break
        elif int(key) == 1:
            print("The show continues...")
        else:
            print("Invalid input. Please press '1' to continue or '0' to exit.")
    except ValueError:
        print("Invalid input. Please enter a number ('0' or '1').")
