env = ["aws","azure","zoho","gcp"]
print(env)

#snake case in python

#env = input() here we are taking input from the user 
# (input is a function to take user input)
#print(env) printing env

uenv = input("enter the env :")
print(uenv)

a = input("enter the number for a :")
b = input("enter the number of b :")

c= a+b
print(c)
# output 
# ['aws', 'azure', 'zoho', 'gcp']
# enter the env :dev
# dev
# enter the number for a :23
# enter the number of b :23
# 2323
#above 2323 we need type casting it is treating it as string
print(type(a))
# ['aws', 'azure', 'zoho', 'gcp']
# enter the env :dev
# dev
# enter the number for a :23
# enter the number of b :23
# 2323
# <class 'str'>


# here we are doing type casting converting one datatype to another
a = int(input("enter the number for a :"))
b = int(input("enter the number of b :"))

c= a+b
print(c)

print("multiplication of a,b :",a*b)
print("addition of a,b:", a+b)

# after type casting output
# python check_env.py
# ['aws', 'azure', 'zoho', 'gcp']
# enter the env :23
# 23
# enter the number for a :23
# enter the number of b :23
# 2323
# <class 'str'>
# enter the number for a :23
# enter the number of b :23
# 46
# PS C:\you work\python\practise> 