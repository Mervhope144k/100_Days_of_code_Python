print("Welcome to Leap year checker!")
print("Enter the year:")
year = int(input())
print(f"The year you entered is {year}")
if(year % 4 == 0):
    if (year % 100 == 0):
        if (year % 400 == 0):
            print(f"{year} is a Leap year")
        else:
            print(f"{year} is not a Leap year")
    else:
        print(f"{year} is a Leap year")
else:
    print(f"{year} is not a Leap year")
