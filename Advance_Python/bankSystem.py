class SBIBank:
    
    def __init__ (self):
        self.name="prathmesh"
        self.accNo=1234
        self.type_acc="saving"
        self.bal_amt=12312
            
    def adddata(self):
        self.name=input("Enter the name : ")
        self.accNo=int(input("Enter the account number : "))
        self.type_acc=input("Enter teh type of account : ")
        self.bal_amt=int(input("Enter the balance amount : "))
        
    def deposit (self):
        dep=int(input("Enter the amount to deposit : "))
        self.bal_amt=self.bal_amt+dep
    
    def display(self):
        print("Name : ",self.name)
        print("Account number :",self.accNo)
        print("Account Type : ",self.type_acc)
        print("Total balance : ",self.bal_amt)
        
    def withdrow (self):
        withdrow_amt=int(input("Enter the amount to withdrow"))
        self.bal_amt=self.bal_amt+withdrow_amt
        
s=SBIBank()
while True:
    print("1. Accept data ")
    print("2. Deposit ")
    print("3. withdraw")
    print("4. Display")
    print("5. Exit")
    
    ch=int(input("Select any choice: "))
    if ch == 1 :
        s.adddata()
    elif ch==2 :
        s.deposit()
    elif ch==3:
        s.withdraw()
    elif ch==4:
        s.display()
    else:
        break



