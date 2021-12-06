import collections
import logging

logging.basicConfig(level=logging.DEBUG)

# Para crear clases sin definición explicita.
Card = collections.namedtuple('Card', ['rank', 'suit'])


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')

    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        '''
        __getitem__ delega en el operador []
        '''
        # logging.info(f'Ranks={self.ranks}')
        # logging.info(f'Suits={self.suits}')
        # logging.info(f'Cards={self._cards}') # Descomentar para ver la lista de elementos.
        return self._cards[position]


deck = FrenchDeck()


def __ejemplos_basicos() -> None:
    beer_card = Card('7', 'diamons')
    print(beer_card)

    print(len(deck))

    print(deck[0])  # Primer elemento. Se utiliza la función __getitem__.
    print(deck[-1])  # Último elemento. Se utiliza la función __getitem__.

    print(f'->{deck[:3]}')

    print('\n-*- Impresión de la baraja en orden ascendente-*-')
    for card in deck:
        print(f'card={card}')
    print('n')

    print('\n-*- Impresión de la baraja en orden descendente-*-')
    for card in reversed(deck):
        print(f'card={card}')
    print('\n')

    print(f'-*- Operación operador in -*-')
    card_aux = Card(rank='Q', suit='hearts')
    print(f'¿{card_aux} in FrechCard? {card_aux in deck}')


def __ordenacion() -> None:
    suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

    def spades_high(card):
        '''
        POdemos realizar estas operaciones porque la clase FrenchCard define las funciones 
        de len y gerittem para conocer la longitug y un elemento determinado.
        Si queremos acceder a un elemento de FrechDeck.ranks.index de forma manual no podemos
        pero, como la clase FrenchCard define estos métodos, podemos utilizarlos.
        '''
        rank_value = FrenchDeck.ranks.index(card.rank)
        return rank_value * len(suit_values) + suit_values[card.suit]

    for card in sorted(deck, key=spades_high):
        print(card)


def run() -> None:
    # __ejemplos_basicos()
    __ordenacion()


if __name__ == '__main__':
    try:
        run()
    except Exception as ex:
        logging.error(f'[ERROR] Example1. Exception=[{ex}]')
