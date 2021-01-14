# Создаем главный клас
class AbstractPizza(object):
    def __init__(self, name: str):
        self._name = name
        self._cost = 10

    @property
    def get_cost(self):
        return f"{self._name} costs {self._cost} $"


class ItalianPizza(AbstractPizza):
    def __init__(self):
        super().__init__('Italian Pizza')

    def __str__(self):
        return self._name

    @property
    def get_cost(self):
        add_cost = self._cost + 5
        return f"{self._name} costs {add_cost} $"


class BulgarianPizza(AbstractPizza):
    def __init__(self):
        super().__init__('Bulgarian Pizza')

    def __str__(self):
        return self._name

    @property
    def get_cost(self):
        add_cost = self._cost + 10
        return f"{self._name} costs {add_cost} $"


# Делаем декоратор
class AbstractAdditive(AbstractPizza):
    def __init__(self, pizza, name):
        super().__init__(name)
        self._name = name
        self._pizza = pizza


class TomatoAdditive(AbstractAdditive):
    def __init__(self, pizza):
        super().__init__(pizza, 'Tomato Additive')
        self._pizza = pizza

    @property
    def get_cost(self) -> str:
        add_cost = self._cost + 15
        return f"{self._pizza} with {self._name} costs {add_cost} $"



class CheeseAdditive(AbstractAdditive):
    def __init__(self, pizza):
        super().__init__(pizza, 'Cheese Additive')
        self._pizza = pizza

    @property
    def get_cost(self) -> str:
        add_cost = self._cost + 25
        return f"{self._pizza} with {self._name} costs {add_cost} $"
