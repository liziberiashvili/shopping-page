class Shop:
    def buy_fruits(self):
        price = 0
        fruits = {
            "apple": 2,
            "banana": 3,
            "orange": 4,
            "watermelon": 10,
            "peach": 1.5
        }
        my_orders = []
        for i in range(len(fruits)):
            a = input(f"We have{fruits},which one do you want?")
            if a == "stop":
                break
            my_orders.append(a)
        print(my_orders)
        for i in my_orders:
            print(i)
            price += fruits.get(i)
        print(price)





shop = Shop()
shop.buy_fruits()