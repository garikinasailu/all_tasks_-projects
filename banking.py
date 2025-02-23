class account:
    def __init__(self,balance=0):
        self.balance=0
    def menu(self):
        print("1.credit amount")
        print("2.debit amount")
        print("3.check_balance")
        print("4.mini statement")
        print("5.logout")
    def choice(self):
        return input("enter your choice(1-5):")
    def credit(self):
        amount=int(input("enter the amount:"))
        if amount<0:
            print("please enter the positive value")
        else:
            self.balance+=amount
            print(f"your amount is {amount}")
    def debit (self):
        amount=int(input("enter the amount:"))
        if amount<0:
            print("please enter the postive value")
        #elif amount>0:
            #print("insufficient amount")
        else:
            self.balance-=amount
            print(f"your debit amount is {amount}")
    def check_balance(self):
        print(f"your balance is {self.balance}")
    def mini_statement(self):
        print("mini_statement")
        print(f"current balance:{self.balance}")
    def logout(self):
        print("-----thank you vist again------")
class bank:
    def __init__(self):
        self.account={}
    def menu(self):
        print("1.create account")
        print("2.login")
        print("3.exit")
    def choice(self):
        return input("enter your choice(1-3):")
    def create_account(self):
        if user_name in self.account:
            print("username already exist")
        else:
            self.account[user_name]=account
        print("account created successfully")
        print("-----welcome python bank-------")
    def login (self):
        if user_name in self.account:
            account=self.account[user_name]
            print("login successfully")
            return account
        else:
            print("invaild username")
        return None
    def exit(self):
        print("---thank you------")
            
bank_system=bank()
while True:
    bank_system.menu()
    choice=bank_system.choice()
    if choice=='1':
        user_name=input("enter your name:")
        password=input("enter your password:")
        bank_system.create_account()
    elif choice=='2':
        user_name=input("enter your name:")
        bank_system.login()
        if account is not None:
            obj=account("0")  
            while True:
               obj.menu()
               choice=obj.choice()
               if choice=='1':
                    obj.credit()
               if choice=='2':
                    obj.debit()
               if choice=='3':
                    obj.check_balance()
               if choice=='4':
                   obj.mini_statement()
               if choice=='5':
                   obj.logout()
                   break
               else:
                    print("invaild choice")
    elif choice=='3':
        bank_system.exit()
        break
    else:
        print("invaild choice")
        


    
