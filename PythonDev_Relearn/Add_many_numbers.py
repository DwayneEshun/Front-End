import math
def add_number(numbers):
    total_ = 0
    for i in numbers:
      total_ += i
    return total_


numbers =[]
while True:
    uinput = input("Do you want to enter a new number? Y/N: " ).upper()
    if uinput == "Y":
        new_num = int(input("Enter a number: "))
        numbers.append(new_num)
    elif uinput == "N":
        break
    else:
        print("Invalid Response")

    
total = add_number(numbers)
print(total)
