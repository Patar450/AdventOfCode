try:
    f = open('Calories.txt','r')
    TotalCalories = f.readlines()
    Elf = 1
    CurrentElfCalories = 0
    PreviousTotalCalories = 0

    for Calories in TotalCalories:
        
        if Calories.isspace() == False:
            CurrentElfCalories += int(Calories)
        else:
            if CurrentElfCalories > PreviousTotalCalories:
                print("Elf number: "+str(Elf)+" Total Calories:"+ str(CurrentElfCalories))
                PreviousTotalCalories = CurrentElfCalories
            Elf +=1
            CurrentElfCalories = 0
finally:
    f.close()