import pytest
from src.classes import Product, Category


@pytest.fixture
def test_list_products():
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
    return product1, product2, product3


def test_product(test_list_products):
    assert test_list_products[0].name == "Samsung Galaxy S23 Ultra"
    assert test_list_products[0].description == "256GB, Серый цвет, 200MP камера"
    assert test_list_products[0].price == 180000.0
    assert test_list_products[0].quantity == 5



@pytest.fixture
def category_smartphones(test_list_products):
    return Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         [test_list_products[0], test_list_products[1], test_list_products[2]])


def test_category(category_smartphones):
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert category_smartphones.products == ["Samsung Galaxy S23 Ultra, 180000.0 руб. Остаток: 5 шт.\n",
 "Iphone 15, 210000.0 руб. Остаток: 8 шт.\n",
 "Xiaomi Redmi Note 11, 31000.0 руб. Остаток: 14 шт.\n"]
    assert category_smartphones.category_count == 1
    assert category_smartphones.product_count == 3
    Category.category_count = 0
    Category.product_count = 0


@pytest.fixture
def category_tvs():
    return Category("Телевизоры",
                         "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
                         ["TV1"])


def test_counts(category_smartphones,category_tvs):
    category_1 = category_smartphones
    category_2 = category_tvs
    assert Category.category_count == 2
    assert Category.product_count == 4
    Category.category_count = 0
    Category.product_count = 0


def test_add_product(category_smartphones):
    category_1 = category_smartphones
    category_1.add_product(Product("55\" QLED 4K", "Фоновая подсветка", 123000.0, 7))
    assert category_1.product_count == 4



@pytest.fixture
def testing_product():
    new_product = Product.new_product(
        {"name": "Samsung Galaxy S23 Ultra", "description": "256GB, Серый цвет, 200MP камера", "price": 180000.0,
         "quantity": 5})
    return new_product


def test_new_product(testing_product):
    assert testing_product.name == "Samsung Galaxy S23 Ultra"
    assert testing_product.description == "256GB, Серый цвет, 200MP камера"
    assert testing_product.price == 180000.0
    assert testing_product.quantity == 5


def test_price_setter(testing_product):
    testing_product.price = 800
    assert testing_product.price == 800
    testing_product.price = 0
    assert testing_product.price == 800
    testing_product.price = -100
    assert testing_product.price == 800
