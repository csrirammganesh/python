import psutil

# take cpu threshold from user
# get current cpu threshold
# if current cpu threshold is more than user input then email 

def check_cpu_threshold():
    user_cpu= float(input("enter the cpu_threshold:"))

    current_cpu= psutil.cpu_percent(interval=1)

    if current_cpu > user_cpu:
        print("cpu Alert email sent") # dummy email
    else:
        print("cpu is fine")
check_cpu_threshold()        
