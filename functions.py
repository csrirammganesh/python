
def sum_of_num(): # fun defination
    num1 = int(input("enter the number:"))
    num2 = int(input("enter the number:"))

    sum = num1 + num2
    print(sum)
env = input("enter the env:")
if env == "prd":
    sum_of_num()
else:
    print("everything is fine")    