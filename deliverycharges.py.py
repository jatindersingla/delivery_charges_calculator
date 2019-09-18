print ("..............................................................")
print("welcome to delivery charges calculator")
print(".......................................")
a = int(input("please enter purchase total: $"))
if a >= 150:
    b = int(input("Please enter number of items: "))
    c = int(input("please enter delivery day ([1] for day and [2] for second day):  "))
    if b<=5:
        if c==1:
            d = a+8
            print("Delivery cost:$8")
            print("Total Cost {:.2f} ".format(d))
        elif c==2:
            e = (b*1.50)
            print("Delivery charges: ${:.2f}".format(e))
            e = e+a
            print("Total cost: ${:.2f}".format(e))
    elif b>=6:
        if c==1:
            f = (b * 2.50)
            print("Delivery charges: ${:.2f}".format(f))
            f = f + a
            print("Total cost: ${:.2f}".format(f))
        elif c==2:
            g = (b * 1.20)
            print("Delivery charges: ${:.2}".format(g))
            g = g + a
            print("Total cost: ${:.2}".format(g))
elif a<=150:
    print("ERR: Sorry purchase total need to be above $150")
h = str(input("Do you want to calculate delivery charges for another purchase? (y/n): "))
if h=="y":
    while (h=="y"):
        a = int(input("please enter purchase total: $"))
        if a >= 150:
            b = int(input("Please enter number of items: "))
            c = int(input("please enter delivery day ([1] for day and [2] for second day):  "))
            if b <= 5:
                if c == 1:
                    d = a + 8
                    print("Delivery cost:$8")
                    print("Total Cost {:.2f} ".format(d))
                elif c == 2:
                    e = (b * 1.50)
                    print("Delivery charges: ${:.2f}".format(e))
                    e = e + a
                    print("Total cost: ${:.2f}".format(e))
            elif b >= 6:
                if c == 1:
                    f = (b * 2.50)
                    print("Delivery charges: ${:.2f}".format(f))
                    f = f + a
                    print("Total cost: ${:.2f}".format(f))
                elif c == 2:
                    g = (b * 1.20)
                    print("Delivery charges: ${:.2}".format(g))
                    g = g + a
                    print("Total cost: ${:.2}".format(g))
        elif a <= 150:
            print("ERR: Sorry purchase total need to be above $150")
        h = str(input("Do you want to calculate delivery charges for another purchase? (y/n): "))

elif h=="n":
    print("Thank for using the delivery charges calculator!")
    print("see you again!")