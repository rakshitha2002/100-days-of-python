year = int(input("Enter the year data to check : "))
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print("Yeah",year,"is leap year.")
else :
    print("Oops",year,"is not a leap year.")