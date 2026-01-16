import random
BankData={}

def createAccount():
    print("===========CREATE NEW ACCOUNT==============")
    print("give me this details:-")
    name=input("enter your name:- ")
    mobile_no=int(input("enter your mobile number:- "))
    Adhar_no=int(input("enter your Adhar number:- "))
    age=int(input("enter your age:- "))
    amount=int(input("enter your amount:- "))
    account_no=random.randint(1000,9999)

    BankData[account_no]={
        "name":name,
        "mobile number":mobile_no,
        "Adhar number":Adhar_no,
        "age":age,
        "amount":amount,
        "account_number":account_no}
    
    print('===================================================')
    print("============account created successfully===========")
    print('account no:- ',BankData[account_no]['account_number'])
    print('====================================================')
    

def deposite():
    print("user want to deposite money")
    # print(BankData)
    acc_no=int(input("enter your account number"))
    if acc_no not in BankData:
        print("not found your account")
    else:
        # print(BankData[acc_no])
        amount=int(input("enter deposite Amount:-"))
        # print(int(BankData[acc_no]['amount'])+amount)=====new amount=======
        BankData[acc_no]['amount']=int(BankData[acc_no]['amount'])+amount
        print("amount deposite successfully")
        print("Total amount is:- ",BankData[acc_no]['amount'])
        

def withdrow():
    print("user want to withdrow money")
        # print(BankData)
    acc_no=int(input("enter your account number"))
    if acc_no not in BankData:
        print("not found your account")
    else:
        # print(BankData[acc_no])
        amount=int(input("enter withdrow Amount:-"))
        # print(int(BankData[acc_no]['amount'])+amount)=====new amount=======
        BankData[acc_no]['amount']=int(BankData[acc_no]['amount']) - amount
        print("amount withdrow successfully")
        print("Remaining Balance is:- ",BankData[acc_no]['amount'])
    

def checkstatement():
    print("user want to check bank statement")
    acc_no=int(input("enter your account number:-"))
    if acc_no not in BankData:
        print("account not found")
    else:
        print("------------ACCOUNT HOLDER DETAILS---------")
        print("name:-",BankData[acc_no]["name"])
        print("mobile number:-",BankData[acc_no]["mobile number"])
        print("Adhar number:-",BankData[acc_no]["Adhar number"])
        print("age:-",BankData[acc_no]["age"])
        print("amount:-",BankData[acc_no]["amount"])
        print("account_number:-",BankData[acc_no]["account_number"])


def updatedetails():
    print("user want to update details")
    acc_no=int(input("enter your account number:-"))
    if acc_no in BankData:
        print("----------SELECT OPTION---------")
        print("1.update your name")
        print("2.update your mobile number")
        print("3.update your Adhar number")
        print("4.update your age")

        choice=int(input("please enter your choice:-"))
        if choice==1:
            print("user want to update name")
            Newname=input("Enter new name:-")
            BankData[acc_no]["name"]=Newname
            print("----------update your name successfully---------")
            print("New name:-",BankData[acc_no]["name"])

        elif choice==2:
            print("user want to update mobile number")
            newmobile_no=int(input("enter new mobile number"))
            BankData[acc_no]["mobile number"]=newmobile_no
            print("---------update your mobile number successfully")
            print("newmobile_no",BankData[acc_no]["mobile number"])

        elif choice==3:
            print("user want to update Adhar number")
            newAdhar_no=int(input("enter new Adhar number"))
            BankData[acc_no]["Adhar number"]=newAdhar_no
            print("---------update your Adhar number successfully")
            print("newAdhar_no",BankData[acc_no]["Adhar number"])

        elif choice==4:
            print("user want to update age")
            newage=int(input("enter new age"))
            BankData[acc_no]["age"]=newage
            print("------update your age successfully------------")
            print("newage",BankData[acc_no]["age"])
        else:
            print("Invalid choice")
    else:
        print("account not found")

def exit():
    print("Thanks for visit")

while True:
    print('====================================')
    print("========WELCOME TO THE BANK=========")
    print("====================================")
    print("\n")
    print("1. for create account:-")
    print("2. for deposite money:-")
    print("3. for withdrow money:-")
    print("4. for check bank statement:-")
    print("5. for update details:-")
    print("6. for exit")
    print("\n")
    choice=int(input("enter your choice:-"))
    if choice==1:
        createAccount()
    elif choice==2:
        deposite()
    elif choice==3:
        withdrow()
    elif choice==4:
        checkstatement()
    elif choice==5:
        updatedetails()
    elif choice==6:
        exit()
        break
    else:
        print("invalid account")