class ATM ():
    def __init__(self,brand):
        brand=brand
    def credit(self,amount):
        print("your amount is credited",amount)
    def debit (self,amount):
        print("your amount is debit",amount)
    def check_balance(self,amount):
        print("your balance",amount)
brand=ATM("sbi")
brand.credit(1000)
brand.debit(400)
brand.check_balance(600)

class laptop ():
    def __init__(self,brand,colour):
       self. brand=brand
       self.colour=colour
    def browsing(self):
        print("your  browsing",brand)
    def game(self):
        print("your gaming")
        self.browsing()
brand=laptop("hp","silver")
brand.browsing()
brand.game()


class atm():
    def __init__(self,brand,pin,phone_number):
        self.brand=brand
        self.pin =pin
        self.phone_number=phone_number
        amount=int(input("enter the amount:"))
        balance=0
class features(atm):
    def credit(self,amount):       
        print(f"your credit amount is {amount}")
    def with_draw(self,amount):
        print(f"your debit amount is {amount}")
    def check_balance(self,amount):
        print(f"your balance{amount}")
obj=features(atm)
self.brand("sbi")
self.pin("123")
self.phone_number(123345678)





    
