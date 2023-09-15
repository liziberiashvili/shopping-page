from utils.DatabaseUtils import DatabaseUtils

class Shop:
    def calculate_price(self):
        basket = []
        select_query = "SELECT ProductName FROM test.product;"

        product_names = DatabaseUtils.select(select_query)
        filtered_products = []
        for i in product_names:
            filtered_products.append(i[0])
        while 2 > 1:
            chosen_product = input(f"We have{filtered_products},which product do you want?")
            if chosen_product not in filtered_products and chosen_product != "x":
                print("We don't have this product")
            elif chosen_product == "x":
                break
            else:
                basket.append(chosen_product)
        print(basket)
        sum = 0
        for i in basket:
            select_price = f"SELECT ProductPrice FROM test.product WHERE ProductName = '{i}';"
            product_price = DatabaseUtils.select(select_price)
            sum += product_price[0][0]
        print(sum)



shop = Shop()
shop.calculate_price()