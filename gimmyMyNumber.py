userString = input("Gimmy a number more than 100 plz ")
userNum = int(userString)

while userNum <= 100:
    print(str(userNum) + " is less than 100...try again...I've got all day. ")
    userString = input("Gimmy a number more than 100 plz ")
    userNum = int(userString)

input("Congrats! " + str(userNum) + " is more than 100! ")
