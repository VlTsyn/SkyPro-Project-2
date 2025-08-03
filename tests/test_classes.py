import pytest
from src.classes import Product, Category


@pytest.fixture
def product_samsung():
    return Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)


def test_product(product_samsung):
    assert product_samsung.name == "Samsung Galaxy S23 Ultra"
    assert product_samsung.description == "256GB, Серый цвет, 200MP камера"
    assert product_samsung.price == 180000.0
    assert product_samsung.quantity == 5



@pytest.fixture
def category_smartphones():
    return Category("Смартфоны",
                         "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
                         ["smartphone1", "smartphone2", "smartphone3"])


def test_category(category_smartphones):
    assert category_smartphones.name == "Смартфоны"
    assert category_smartphones.description == "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни"
    assert category_smartphones.products == ["smartphone1", "smartphone2", "smartphone3"]
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