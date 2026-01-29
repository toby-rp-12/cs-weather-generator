import random

print("Welcome to weather generator!")
print("Enter the number of days you want us to generate weather for.")
days = int(input(">")) + 1
print("Enter the lowest you want the temprature to go to.")
while True:
    try:
        low = int(input(">"))
        if low <= -460:
            print("Enter a temprature above absolute 0:")
        else:
            break
    except ValueError:
        print("WRITE A NUMBER, IT'S NOT THAT HARD:")
        continue
print("Enter the highest you want the temprature to go to.")
while True:
    try:
        high = int(input(">"))
        if high <= low:
            print("Enter a value above ", low, ":")
        else:
            break
    except ValueError:
        print("WRITE A NUMBER, IT'S NOT THAT HARD:")
        continue
for i in range(1, days):
    print("Day", str(i), ":", str(random.randint(low, high)), "° F")
print("Thank you for using weather generator! Restart the program to go again.")
