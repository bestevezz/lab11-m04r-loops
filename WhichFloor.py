userString = input("Which floor do you work on? ")
userNum = int(userString)
max_floors = 60

while userNum >= max_floors:
    print(str(userNum) + " is not even a floor... Do you work here? ")
    userString = input("Which floor do you work on? ")
    userNum = int(userString)

input("Congrats! " + str(userNum) +
      " is definitely a floor I know! Great department! ")
