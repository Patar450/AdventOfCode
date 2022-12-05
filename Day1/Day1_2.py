try:
    #Open Calories.txt and will read the line to a variable TotalCalories
    fr = open('Calories.txt','r')
    TotalCalories = fr.readlines()
    #This list will be used to store the total calorie of each elf.
    listOfAllElfs= []

    CurrentElfCalories = 0

    #for loop will read each line in the txt one by one.
    #each Calorie will be added to the CurrentElfCalorie variable
    #When the readline see an empty line then the CurrentElfCalorie will be added in the index of the listOfAllElfs
    for Calories in TotalCalories:
        if Calories.isspace() == False:
            CurrentElfCalories += int(Calories)
        else:
            listOfAllElfs.append(CurrentElfCalories)
            CurrentElfCalories = 0    
    
    #sort the list in ascending order
    listOfAllElfs.sort()

    #loop to remove the first element untill the size of the list is reduced to 3
    while len(listOfAllElfs) != 3:
        listOfAllElfs.pop(0)

    #Variable to use for the coming for loop
    TotalCaloriesWithTopThreeElves = 0

    #for loop to get the total of all 3 highest total calories
    for top3Calories in listOfAllElfs:
        TotalCaloriesWithTopThreeElves += top3Calories
    
    #prints the highest Calorie one of the elfs are carrying
    print("Elf with the highest Calories has a total of: "+ str(listOfAllElfs[2]))

    #display the total of all 3 highest calories that the top elfs are carying altogether
    print("Total Calories for the top 3 Calories holding elfs is: ", str(TotalCaloriesWithTopThreeElves))

finally:
    #close fileRead
    fr.close()
