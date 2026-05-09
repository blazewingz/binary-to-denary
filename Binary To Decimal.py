binary = input("Enter a binary number: ")
idx = 0
valid = True   # we can only hope

values = []  # Store Values to then add later

# valid check
for i in range(len(binary)):
    if binary[idx] != "0" and binary[idx] != "1":
        valid = False
    idx = idx + 1   # move idx thru the array

# main checker
idx = 0  # clear cache, resuing the same variable

if valid == True:
 while idx < len(binary) and valid:  # only run if valid
     digit = int(binary[idx])  # cycle thru items in array

     power = len(binary) - 1 - idx
    
     value = digit * (2 ** power)
     values.append(value)
    
     idx = idx + 1

# Add Values cuz we can
decimal = sum(values)

if valid == True:
    print("Decimal value:", decimal)
elif valid == False:
    print(binary, "is not Valid Binary!")

SystemExit