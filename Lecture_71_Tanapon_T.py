menuList = []
priceList = []

def showBill():
    print("----My Food----")
    totalPrice = 0
    for number in range(len(menuList)):
        print(menuList[number],priceList[number],"THB")
        totalPrice = totalPrice + int(priceList[number])
    print("Total Price Is : ",totalPrice,"THB")


while True:
    menuName = str(input("Please Enter Menu : "))
    if menuName.lower() == "exit":
        break
    else:
        menuPrice = str(input("Please Enter Price : "))
        menuList.append(menuName)
        priceList.append(menuPrice)

showBill()

