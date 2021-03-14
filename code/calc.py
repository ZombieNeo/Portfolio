print("WELCOME TO THE CALCULATOR")
number=input
number1=input
answer=input
custom=input
option=input("please choose option (1= time. 2= divide.3=add.4=minus.5=squaring.6=cubing.7=custom square) ")#at soempoint needs loop
print("\n")
print("you have choosen option "+(option))

if option == "1":
    number=input("enter number one ")
    print(number)
    number1=input("enter number two ")
    print(number1)
    answer=float(number)*float(number1)
    print(str(number)+"x"+str(number1)+"="+str(answer))#this segment works
    
if option == "2":
    number=input("enter number one ")
    print(number)
    number1=input("enter number two ")
    print(number1)
    answer=float(number)/float(number1)
    print(str(number)+"/"+str(number1)+"="+str(answer))


if option == "3":
    number=input("enter number one ")
    print(number)
    number1=input("enter number two ")
    print(number1)
    answer=float(number)+float(number1)
    print(str(number)+"+"+str(number1)+"="+str(answer))
    
if option == "4":
    number=input("enter number one ")
    print(number)
    number1=input("enter number two ")
    print(number1)
    answer=float(number)-float(number1)
    print(str(number)+"-"+str(number1)+"="+str(answer))

if option == "5":
    number=input("enter number to be squared ")
    print(number)
    answer=float(number)*float(number)
    print(str(number)+"**"+str(number)+"="+str(answer))

if option == "6":
    number=input("enter number to cubed")
    print(number)
    answer=float(number)*float(number)*float(number)
    print(str(number)+"***"+str(number)+"="+str(answer))

if option == "7":#makes number get timesed my number amount user enters
     print("OK THIS IS VERY NAFF to get answer choose number to be X by itself eg in first box type 9 and in box two enter how many times you want it to be x by itself so if you entered 9 in first box and 9 in secon it will be 9X9X9") 
     number=input("enter number one ")
     print(number)
     number1=(number)
     print(number1)#works
     custom=input("how many times do you wnat that X by itself?")
     answer=float(number) *float(number1)*float(custom)
     print(str(number)+"x^y"+str(number1)+"="+str(answer))    