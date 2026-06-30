print("---Super Market Billing System---")   #headline
print("")

#variables
tot = 0
count = 0
item_list = []

#get inputs
items = int(input("How many items are buying? : "))

if items == 0:   #check user wants to continue
    print("BYE!!")

else:
    name = input("Enter item name: ")
    price = float(input("Enter item price: Rs."))
    qnty = int(input("Enter the quantity: "))

    item_list.append(name)   #adding 1st input to the list

    tot = (price * qnty)

    #variables for expensive item
    expensive_item = price
    expensive_item_name = name
    expensive_item_price = (price * qnty)

    while count < (items-1):   #starting while loop
        name = input("\nEnter item name(q to quite): ")

        if name.lower() != "q":   #check user wants to continue
            price = float(input("Enter item price: Rs."))
            qnty = int(input("Enter the quantity: "))

            item_list.append(name)   #adding other inputs to list

            tot = tot + (price * qnty)

            if price >= expensive_item:   #compare the price with 1st input
                expensive_item = price
                expensive_item_name = name
                expensive_item_price = (price * qnty)   

        else:
            print("BYE!!")

        count = count + 1

    print("")   ##For fun part
    num = int(input("Enter your mobile number(1,2,3,4): "))

    if num == 1:
        name1 = "Nirodhya"
    elif num == 2:
        name1 = "Mohan"
    elif num == 3:
        name1 = "Vihangi"
    else:
        name1 = "MS"

    print("________________________________________________________________________________")
    print("")
    print(f"***Hello {name1}!!***")
    print("")
    print(f"**Total Bill -> Rs.{tot}/=")
    print("")
    print(f"**The most expensive item -> {expensive_item_name} | Rs.{expensive_item_price}/=")
    print("")
    print(f"**List of items\n {item_list}")
    print("")
    print(f"**Thank you! Have a great day {name1}!!!")
    print("________________________________________________________________________________")


    




    

