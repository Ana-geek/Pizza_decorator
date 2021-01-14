from models import *

"""
Вам необходимо прописать реализацию 
паттерна Деĸоратор на примере пицерии.
"""

if __name__ == '__main__':
    pizza = AbstractPizza('Ordinary Pizza')
    print(pizza.get_cost)
    print('>' * 40)
    pizza_it = ItalianPizza()
    print(pizza_it.get_cost)
    print('>' * 40)
    pizza_b = BulgarianPizza()
    print(pizza_b.get_cost)
    print('>' * 40)
    pizza_b_t = TomatoAdditive(pizza_it)
    print(pizza_b_t.get_cost)
    print('>' * 40)
    pizza_with_cheese = CheeseAdditive(pizza_b)
    print(pizza_with_cheese.get_cost)
