class OnlineShop:
    def __init__(self, producy_name, price, quantity):
        self.p_name = producy_name
        self.price = price
        self.quanty = quantity

    def total_price(self):
        print(f"umumiy narx: {self.price}")

    def apply_discount(self, percent):
        self.percent = percent

        if self.price > 100000:
            print(f"chegirmasi: {self.price - 35}")

k2 = OnlineShop("Uzum", 150000, 35)
k2.total_price()
