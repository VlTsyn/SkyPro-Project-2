from abc import ABC, abstractmethod


class BaseProduct(ABC):
    """Базовый абстрактный класс для продуктов"""

    @abstractmethod
    def new_product(self, product):
        pass

    @abstractmethod
    def price(self):
        pass


class MixinLog:
    """Класс логирования при инициализации объекта"""

    def __init__(self):
        self.order_log()
        super().__init__()

    def order_log(self):
        print(f"{self.__class__.__name__}('{self.name}', '{self.description}', {self.price}, {self.quantity})")


class Product(MixinLog, BaseProduct):
    """Родительский класс для продуктов"""
    name: str
    description: str
    __price: float
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity
        super().__init__()

    def __str__(self):
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if isinstance(other, self.__class__):
            result = self.quantity * self.price + other.quantity * other.price
            return result

        raise TypeError

    @classmethod
    def new_product(cls, product):
        return cls(**product)

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, new_price):
        if new_price > 0:
            self.__price = new_price
        else:
            print("Цена не должна быть нулевая или отрицательная")


class Category:
    """Класс для категорий"""
    name: str
    description: str
    __products: list
    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products
        self.product_count = len(products)
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        result = 0
        for product in self.__products:
            result += product.quantity
        return f"{self.name}, количество продуктов {result} шт."

    def add_product(self, product):
        if issubclass(type(product), Product):
            self.product_count += 1
            Category.product_count += 1
            return self.__products.append(product)

        raise TypeError

    @property
    def products(self):
        result = []
        for product in self.__products:
            result.append(f"{product.name}, {product.price} руб. Остаток: {product.quantity} шт.\n")
        return result


class Smartphone(Product):
    """Подкласс продуктов смартфонов"""
    efficiency: float
    model: str
    memory: float
    color: str

    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color


class LawnGrass(Product):
    """Подкласс продуктов газонной травы"""
    country: str
    germination_period: str
    color: str

    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
