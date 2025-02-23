

name=(input("enter the name:"))
lists='''
rice i   RS 10/kg
oil     RS 30/liters
milk    RS 1packet
panner  RS 250 grams
'''

items={"rice":100,"oil":45,"milk":35,"panner":60}
price=0
while True:

    choice=int(input("enter the choice:"))
    if  choice==1:
        item=(input("enter the your items : "))
        quantity=int(input("enter the quantites:"))

    
     
    if item in items:
       
        total_price=quantity*items[item]
        print("_"*20)
        print(f"{item}:  {total_price}")
        print("_"*20)
        print(price)

    if choice==2:
        print("tankyou visit the shopping")