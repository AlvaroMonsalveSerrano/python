
'''
Ejemplo muy parecido a chapter6.example1 pero usando decoradores.
'''
import logging
from collections import namedtuple

from module_decorators import promotion
# from chapter6.example1 import Order, Customer, LineItem
# import chapter6.example1 as domain


Customer = namedtuple('Customer', 'name fidelity')


class LineItem:

    def __init__(self, product, quantity, price):
        self.product = product
        self.quantity = quantity
        self.price = price

    def total(self):
        return self.price * self.quantity


class Order:  # El contexto

    def __init__(self, customer, cart, promotion=None):
        self.customer = customer
        self.cart = cart
        self.promotion = promotion

    def total(self):
        if not hasattr(self, '__total'):
            self.__total = sum(item.total() for item in self.cart)
        return self.__total

    def due(self):
        if self.promotion is None:
            discount = 0
        else:
            discount = self.promotion(self)

        return self.total() - discount

    def __repr__(self) -> str:
        fmt = '<Order total: {:.2f} due: {:.2f}>'
        return fmt.format(self.total(), self.due())


@promotion
def fidelity_promo(order: Order):
    ''' 5% de descuento para clientes con 1000 o más puntos de fidelidad.'''
    return order.total() * 0.5 if order.customer.fidelity >= 1000 else 0


@promotion
def bulk_item_promo(order: Order):
    '''10% de descuento para cada LineItem con 20 o más unidades.'''
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


@promotion
def large_order_promo(order: Order):
    '''7% de descuento para ordenes con 10 o más items distintos'''
    distincts_items = {item.product for item in order.cart}
    if len(distincts_items) >= 10:
        return order.total() * 0.7
    return 0


def run() -> None:
    joe = Customer(name='John Doe', fidelity=0)
    ann = Customer(name='Ann Smith', fidelity=1100)
    cart = [
        LineItem(product='banana', quantity=4, price=.5),
        LineItem(product='apple', quantity=10, price=1.5),
        LineItem(product='watermellon', quantity=5, price=5.0)
    ]
    print(f'-*- Patrón strategie con funciones -*-')
    # OJO! Asignación de la función con la estrategia de promoción fidelity_promo al contexto.
    order_joe = Order(customer=joe, cart=cart, promotion=fidelity_promo)
    print(f'order_joe={order_joe}')

    order_ann = Order(customer=ann, cart=cart, promotion=fidelity_promo)
    print(f'order_ann={order_ann}')

    banana_cart = [
        LineItem(product='banana', quantity=30, price=.5),
        LineItem(product='apple', quantity=10, price=1.5)
    ]

    order_joe_2 = Order(customer=joe, cart=banana_cart,
                        promotion=bulk_item_promo)
    print(f'order_joe_2={order_joe_2}')

    long_order = [LineItem(str(item_code), 1, 1.0) for item_code in range(10)]
    order_joe_3 = Order(customer=joe, cart=long_order,
                        promotion=large_order_promo)
    print(f'order_joe_3={order_joe_3}')

    order_joe_4 = Order(customer=joe, cart=cart, promotion=large_order_promo)
    print(f'order_joe_4={order_joe_4}')


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
