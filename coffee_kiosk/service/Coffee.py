class Coffee:
    # Coffee 생성자에서 이름, 재고, 매입비용, 판매비용 등등을 생성
    def __init__(self, name, stock, sales_cnt, safety_stock, cost, price):
        self._name = name
        self._stock = stock
        self._sales_cnt = sales_cnt
        self._safety_stock = safety_stock
        self._cost = cost
        self._price = price

    def offer(self, order_cnt):
        pass

    def add_stock(self, cnt):
        self._stock += cnt


    # 아래는 모두 getter이다. 아직 커피 이름이나 재고를 set 하는 기능은 없다.
    def get_name(self):
        return self._name
    
    def get_stock(self):
        return self._stock
    
    def get_sales_cnt(self):
        return self._sales_cnt
    
    def get_safety_stock(self):
        return self._safety_stock
    
    def get_cost(self):
        return self._cost
    
    def get_price(self):
        return self._price

    def __str__(self):
        return (
            "Coffee [name="
            + self._name
            + ", stock="
            + str(self._stock)
            + ", totalSalesCnt="
            + str(self._sales_cnt)
            + ", safetyStock="
            + str(self._safety_stock)
            + ", cost="
            + str(self._cost)
            + ", price="
            + str(self._price)
            + "]"
            )