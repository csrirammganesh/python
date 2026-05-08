for i in range (1,5):
    env = input("enter the env :")

    print("user entered env is :", env)

    if env == "prd":
        print("deploy on monday")
    elif env == "stg":
        print("test the stage well and take backup")
    else:
        print("deploy on any day")
