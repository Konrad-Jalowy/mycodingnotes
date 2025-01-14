class OrderItem:
    def __init__(self, product_id: int, quantity: int, price: float):
        self.product_id = product_id
        self.quantity = quantity
        self.price = price

    def total_price(self):
        return self.quantity * self.price


class Order:
    def __init__(self, order_id: int):
        self.order_id = order_id
        self.items = []

    def add_item(self, item: OrderItem):
        self.items.append(item)

    def total_price(self):
        return sum(item.total_price() for item in self.items)


# Przykład użycia
order = Order(1)
order.add_item(OrderItem(101, 2, 19.99))
order.add_item(OrderItem(102, 1, 29.99))

print(order.total_price())  # Output: 69.97
