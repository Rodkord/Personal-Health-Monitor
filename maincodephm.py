while True:
    print("*" * 35)
    print("     PERSONAL HEALTH MONITOR")
    print("*" * 35)
    print()

    print("1. BMI Calculator")
    print("2. Water Intake Tracker")
    print("3. Calories Counter")
    print("4. Blood Information")
    print("5. Exit")
    print()

    opt = input("Please choose an option (1-5): ")

    # BMI CALCULATOR
    if opt == "1":
        print("\nBMI Calculator\n")

        weight = float(input("Enter your Weight (kg): "))
        if weight <= 0:
            print("Weight must be greater than 0.")
            continue

        height = float(input("Enter your Height (m): "))
        if height <= 0:
            print("Height must be greater than 0.")
            continue

        bmi = weight / (height ** 2)

        print("\n===== BMI REPORT =====")
        print(f"Weight : {weight} kg")
        print(f"Height : {height} m")
        print(f"BMI    : {bmi:.2f}")

        if bmi < 18.5:
            print("Condition: UNDERWEIGHT")
        elif bmi < 25:
            print("Condition: NORMAL WEIGHT")
        elif bmi < 30:
            print("Condition: OVERWEIGHT")
        else:
            print("Condition: OBESITY")

        print()

    #  WATER INTAKE TRACKER 
    elif opt == "2":
        print("\nWater Intake Tracker\n")

        weight = float(input("Enter your Weight (kg): "))
        if weight <= 0:
            print("Weight must be greater than 0.")
            continue

        recommended = (weight * 35) / 1000

        print(f"\nRecommended Daily Water Intake: {recommended:.2f} L")

        glasses = int(input("How many glasses have you drunk today? "))
        glass_size = float(input("Size of each glass (ml): "))

        consumed = (glasses * glass_size) / 1000

        print(f"\nWater Consumed : {consumed:.2f} L")

        remaining = recommended - consumed

        if remaining > 0:
            print(f"Remaining Water: {remaining:.2f} L")
        else:
            print("Congratulations! Daily water goal reached.")

        progress = (consumed / recommended) * 100

        if progress > 100:
            progress = 100

        print(f"Progress: {progress:.1f}%")
        print()

    #  CALORIES COUNTER 
    elif opt == "3":
        print("\nCalories Counter\n")

        breakfast = float(input("Breakfast Calories: "))
        lunch = float(input("Lunch Calories: "))
        dinner = float(input("Dinner Calories: "))
        snacks = float(input("Snacks Calories: "))

        total = breakfast + lunch + dinner + snacks

        print("\n===== DAILY CALORIE REPORT =====")
        print(f"Breakfast : {breakfast:.0f} kcal")
        print(f"Lunch     : {lunch:.0f} kcal")
        print(f"Dinner    : {dinner:.0f} kcal")
        print(f"Snacks    : {snacks:.0f} kcal")
        print("-------------------------------")
        print(f"Total Calories : {total:.0f} kcal")

        if total < 1800:
            print("Status: Low Calorie Intake")
        elif total <= 2500:
            print("Status: Healthy Calorie Intake")
        else:
            print("Status: High Calorie Intake")

        print()

    #  BLOOD INFORMATION
    elif opt == "4":
        print("\nBlood Information\n")

        blood = input("Enter your Blood Group (A+, A-, B+, B-, AB+, AB-, O+, O-): ").upper()

        if blood == "O-":
            print("\nBlood Group :", blood)
            print("Can Donate To    : Everyone")
            print("Can Receive From : O-")

        elif blood == "O+":
            print("\nBlood Group :", blood)
            print("Can Donate To    : O+, A+, B+, AB+")
            print("Can Receive From : O+, O-")

        elif blood == "A-":
            print("\nBlood Group :", blood)
            print("Can Donate To    : A-, A+, AB-, AB+")
            print("Can Receive From : A-, O-")

        elif blood == "A+":
            print("\nBlood Group :", blood)
            print("Can Donate To    : A+, AB+")
            print("Can Receive From : A+, A-, O+, O-")

        elif blood == "B-":
            print("\nBlood Group :", blood)
            print("Can Donate To    : B-, B+, AB-, AB+")
            print("Can Receive From : B-, O-")

        elif blood == "B+":
            print("\nBlood Group :", blood)
            print("Can Donate To    : B+, AB+")
            print("Can Receive From : B+, B-, O+, O-")

        elif blood == "AB-":
            print("\nBlood Group :", blood)
            print("Can Donate To    : AB-, AB+")
            print("Can Receive From : AB-, A-, B-, O-")

        elif blood == "AB+":
            print("\nBlood Group :", blood)
            print("Can Donate To    : AB+")
            print("Can Receive From : Everyone")

        else:
            print("\nInvalid Blood Group!")

        print()

    # EXIT 
    elif opt == "5":
        print("\nThank you for using Personal Health Monitor.")
        break

    # INVALID OPTION
    else:
        print("\nInvalid option! Please choose a number between 1 and 5.\n")
