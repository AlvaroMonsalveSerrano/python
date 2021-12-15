'''
Ejemplo de definición del patron strategie con funciones.
'''
import logging
import inspect

from collections import namedtuple


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

# Definición de las estrategias de descuento. -------------------------------
# Funciones que sustituyen al patrin strategie en objetos.


def fidelity_promo(order: Order):
    ''' 5% de descuento para clientes con 1000 o más puntos de fidelidad.'''
    return order.total() * 0.5 if order.customer.fidelity >= 1000 else 0


def bulk_item_promo(order: Order):
    '''10% de descuento para cada LineItem con 20 o más unidades.'''
    discount = 0
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * .1
    return discount


def large_order_promo(order: Order):
    '''7% de descuento para ordenes con 10 o más items distintos'''
    distincts_items = {item.product for item in order.cart}
    if len(distincts_items) >= 10:
        return order.total() * 0.7
    return 0
# -----------------------------------------------------------------------------


def __example1() -> None:
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

    promotions = ['fidelity_promo', 'bulk_item_promo', 'large_order_promo']
    print(f'promotions={promotions}')
    # Los módulos son también First-Class objects. Búsqueda por nombre en el presente módulo.
    promos = [globals()[name] for name in globals()
              if name.endswith('_promo') and name != 'best_promo'
              ]
    print(f'promos={promos}')

    # Cálculo de la función por introspección.
    # from chapter5.example1 import example1
    # promos2 = [func for name, func in inspect.getmembers(
    #     example1, inspect.isfunction)]

    # print(f'promos2={promos2}')


def __command1() -> None:
    print(f'\nComand1!!\n')


def __command2() -> None:
    print(f'\nComand2!!\n')


def __command3() -> None:
    print(f'\nComand3!!\n')


class MacroCommand:
    """Comando que ejecuta una lista de comandos.
    """

    def __init__(self, *commands) -> None:
        self.commands = list(commands)

    def __call__(self):
        for command in self.commands:
            command()


def __example2() -> None:
    print(f'-*- Ejemplos de Comand -*-')

    macro_command = MacroCommand(__command1, __command2, __command3)
    macro_command()


def run() -> None:
    __example1()
    __example2()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
