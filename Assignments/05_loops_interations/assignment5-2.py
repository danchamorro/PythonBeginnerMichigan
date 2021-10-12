# 5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. Once 'done' is entered, print
# out the largest and smallest of the numbers. If the user enters anything other than a valid number catch it with a try/except and put
# out an appropriate message and ignore the number. Enter 7, 2, bob, 10, and 4 and match the output below.


largest = None
smallest = None
while True:
    snum = input("Enter a number: ")
    if snum == "done":
        break
    try:
        inum = int(snum)
    except:
        print("Invalid input")
        continue
    num_list = []
    num_list.append(inum)
    for num in num_list:
        if largest is None:
            largest = num
        elif num > largest:
            largest = num
    for num in num_list:
        if smallest is None:
            smallest = num
        elif num < smallest:
            smallest = num

print("Maximum is", largest)
print("Minimum is", smallest)
