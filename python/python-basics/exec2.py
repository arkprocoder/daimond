import time

itemsCart=[]
itemPrice=[]


def orderitem(item,price):
    itemsCart.append(item)
    itemPrice.append(price)
    print(f"Your item {item} has been added to cart")
    time.sleep(2)
    menu()

def placeorder():
    print("Your Ordered items are ")
    for i in itemsCart:
        time.sleep(0.5)
        print(i)
    print("Total bill is ",sum(itemPrice))
    time.sleep(2)
    print("Thanks for the Order")

def menu():
    print("Order menu")
    time.sleep(0.5)    
    print("1. Dosa")
    time.sleep(0.5)
    print("2. Idli")
    time.sleep(0.5)
    print("3. Pizza")
    time.sleep(0.5)
    print("4. Burger")
    time.sleep(0.5)
    print("5. Chicken grill")
    time.sleep(0.5)
    print("6. Biryani")
    time.sleep(0.5)
    print("7. Ice Cream")
    time.sleep(0.5)
    print("8. Place order")
    order=int(input("Select the menu items:\n"))
    if order>0 and order<9:
        if order==1:
            orderitem("Dosa",80)
        elif order==2:
            orderitem("Idli",40)
        elif order==3:
            orderitem("Pizza",200)
        elif order==4:
            orderitem("Burger",150)
        elif order==5:
            orderitem("Chicken grill",340)
        elif order==6:
            orderitem("Biryani",150)
        elif order==7:
            orderitem("Ice Cream",80)
        elif order==8:
            placeorder()
        else:
            pass
    else:
        print("Please select only 1-8 items from the menue")
        menu()  

menu()