num = int(input("enter the number you want table for:"))

print("user input number is :",num)
# string formatting
for i in range(1,11):
    print( f"{num} x {i} = {num*i}")