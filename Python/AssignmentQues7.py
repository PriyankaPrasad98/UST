#7. Ask user to input email and check if the email is in valid form or not. Ex: it should contain single '@', '.', @or.shouldn't be in 1st position



mail=input("Enter Your mail id \n")
count=0
if ((mail[0]!='@') and (mail[0]!=".")):
    for i in mail:
        if ((i == '@')or (i == '.')):
            count+=1
            if(count>=3):
                break
if (count==2):
    print("Valid mail id")
else:
    print("Invalid mail id ")
