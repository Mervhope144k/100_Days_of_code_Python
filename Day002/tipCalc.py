print("Welcome to the tip calculator!")
TotalBill = input("What was the total bill? $" )
TipPercentage = input("How much tip would you like to give? 10, 12, or 15? " )
NumberOfPeople = input("How many people to split the bill? " )
TotalWithTip = round((float(TotalBill) * ((int(TipPercentage)/100) + 1))/int(NumberOfPeople),2)
print(f"Each person should pay: ${TotalWithTip:.2f}")

