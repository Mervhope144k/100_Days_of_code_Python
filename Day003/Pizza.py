print("Thank you for choosing Python Pizza Deliveries!")
print("Enter your Pizza's size: 'L', 'M' or 'S'")
size = input()
print("Would you like to add pepperoni? 'Y' or 'N'")
add_pepperoni = input()
print("Would you like to add Extra cheese? 'Y' or 'N'")
extra_cheese = input()
bill = 0
if (size == 'S'):
    bill += 15
    # if(add_pepperoni == 'Y'):
    #     bill += 2
    # if(extra_cheese == 'Y'):
    #     bill += 1
elif (size == 'M'):
    bill += 20
    # if(add_pepperoni == 'Y'):
    #     bill += 3
    # if(extra_cheese == 'Y'):
    #     bill += 1
elif (size == 'L'):
    bill = 25
    # if(add_pepperoni == 'Y'):
    #     bill += 3
    # if(extra_cheese == 'Y'):
    #     bill += 1
if(add_pepperoni == 'Y'):
    if (size == 'S'):
        bill += 2
    else:
        bill += 3
if(extra_cheese == 'Y'):
    bill += 1
print("Thank you for choosing Python Pizza Deliveries!")
print(f"Your final bill is: ${bill}")