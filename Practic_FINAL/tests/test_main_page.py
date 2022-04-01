import time
import pytest
from config import *
from pages.main_page import MainPage


def generate_string(b: int):
    """Функция генератор строки заданной длины"""
    s = "a" * b
    print(s)
    return s


def test_search_king(testing_driver):
    """Проверка поиска книг автора "Стивен кинг" """
    page_one = MainPage(testing_driver)
    page_one.input_search.send_keys("Стивен Кинг")
    page_one.btn_search.click()
    # проверка, что на открытой странице есть элементы
    assert page_one.products_titles_king.count() > 0
    # Проверяем наличие книг автора
    for title in page_one.products_titles_king.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'кинг' in title.lower(), msg

    assert page_one.get_current_url() == 'https://www.labirint.ru/search/%D0%A1%D1%82%D0%B8%D0%B2%D0%B5%D0%BD%20%D0%9A%D0%B8%D0%BD%D0%B3/?stype=0'


def test_check_wrong_input_search_king(testing_driver):
    """Проверка поиска с неправильной раскладкой"""
    page = MainPage(testing_driver)
    page.input_search.send_keys("Cnbdty Rbyu")  # "Стивен Кинг"
    page.btn_search.click()
    # проверка, что на открытой странице есть элементы
    assert page.products_titles_king.count() > 0

    for title in page.products_titles_king.get_text():
        message_error = 'Wrong product in search "{}"'.format(title)
        assert 'кинг' in title.lower(), message_error


def test_filter_presence(testing_driver):
    """ Проверка кнопки фильтра "В наличии """
    page = MainPage(testing_driver)
    page.input_search.send_keys("Анджей Сапковский")
    page.btn_search.click()

    if page.products_titles.count() > 0:
        page.btn_filter_presence.click()
    else:
        print("Список пуст")

    assert page.products_titles.count() > 0
    for title in page.products_titles.get_text():
        message_er = 'Wrong product in search "{}"'.format(title)
        assert 'сапковский' in title.lower(), message_er


def test_add_book_to_cart(testing_driver):
    """ Добавлеие товара в корзину """
    page = MainPage(testing_driver)
    page.input_search.send_keys("Ведьмак")
    page.book_vedmak.scroll_to_element()
    page.btn_search.click()

    page.btn_to_cart.scroll_to_element()
    page.btn_to_cart.click()
    page.scroll_up()
    page.btn_ofform_close.click()
    page.cart_btn.click()
    # Проверка перехода на страницу "Корзина"
    assert page.get_current_url() == 'https://www.labirint.ru/cart/'
    text_v = page.book_vedmak_cart.get_text()
    print(text_v)  # Ведьмак. Меч Предназначения
    # Проверка что книга добавлена
    assert 'ведьмак' in text_v.lower()


def test_valid_my_lab(testing_driver):
    """ Авторизация пользователя c валидными данными """
    page = MainPage(testing_driver)
    page.btn_my_lab.click()
    time.sleep(2)
    page.fild_email.click()
    page.fild_email.send_keys(valid_email)
    page.btn_enter.click()
    time.sleep(2)
    page.email_pod.find()
    my_email = page.email_pod.get_attribute('value')

    assert my_email == valid_email

    page.input_code_email.click()
    page.input_code_email.send_keys(email_code_enter)
    page.button_assert_and_enter.click()


def test_personal_account(testing_driver):
    """"Проверка соответствия данных в личном кабинете"""
    page = MainPage(testing_driver)
    page.btn_my_lab.click()
    time.sleep(2)
    page.fild_email.click()
    page.fild_email.send_keys(valid_email)
    page.btn_enter.click()
    time.sleep(2)

    page.input_code_email.click()
    page.input_code_email.send_keys(email_code_enter)
    page.button_assert_and_enter.click()
    time.sleep(6)
    page.btn_my_lab_cabinet.wait_to_be_clickable(10)
    page.btn_my_lab_cabinet.click()
    page.btn_my_data_and_options.click()
    value_my_email = page.data_email.find().get_attribute('value')

    assert value_my_email == valid_email


def test_page_contained_images(testing_driver):
    '''Проверка наличия фото у всех книг на странице по запросу поиска "Ведьмак" '''

    page = MainPage(testing_driver)
    page.input_search.send_keys("Ведьмак")
    page.btn_search.click()
    images = page.images_all_book_vedmak.find()

    for i in range(len(images)):
        assert images[i].get_attribute('src') != ""


def test_page_price_all_books(testing_driver):
    '''Проверка наличия цены у всех книг на странице по запросу поиска "Ведьмак" '''

    page = MainPage(testing_driver)
    page.input_search.send_keys("Ведьмак")
    page.btn_search.click()
    price = page.all_price_vedmak.find()

    for i in range(len(price)):
        assert price[i].get_attribute('data-price') != ""


def test_page_description_books(testing_driver):
    """Проверка наличия названия у всех книг на странице по запросу поиска "Ведьмак" """

    page = MainPage(testing_driver)
    page.input_search.send_keys("Ведьмак")
    page.btn_search.click()
    name = page.name_all_book_vedmak.find()

    for i in range(len(name)):
        assert name[i].text != ''


def test_add_book_defer(testing_driver):
    """Проверка добавления книги в "Отложено" авторизованного пользователя"""

    page = MainPage(testing_driver)
    page.btn_my_lab.click()
    time.sleep(2)
    page.fild_email.click()
    page.fild_email.send_keys(valid_email)
    page.btn_enter.click()
    time.sleep(2)
    page.email_pod.find()
    my_email = page.email_pod.get_attribute('value')

    assert my_email == valid_email

    page.input_code_email.click()
    page.input_code_email.send_keys(email_code_enter)
    page.button_assert_and_enter.click()
    time.sleep(7)
    page.input_search.send_keys("Python")
    page.btn_search_two.click()
    page.basket.scroll_to_element()
    title_book_python = page.python_book.get_attribute('data-name')
    print(title_book_python.lower())  # Python. Искусственный интеллект, большие данные и облачные вычисления

    page.like_defer.click()
    page.btn_pending.scroll_to_element()
    page.btn_pending.click()
    page.book_python_pending.scroll_to_element()
    title_book_pending = page.book_python_pending.get_attribute('data-name')
    print(title_book_pending.lower())

    page.like_button.click()

    assert title_book_pending == title_book_pending, "Книга не добавлена в отложено"


@pytest.mark.parametrize("negativ_email", [" ", "hello", "gunyaga@ya", "!2@^^&*098", "+7123456", "Почта", "你好！"])
def test_not_valid_my_lab(backdrop_testing_driver, negativ_email):
    """ Негативный тест авторизации пользователя c  не валидными данными.
     При вводе не валидных данных кнопка "Войти" не активная
     Запуск осуществляется в фоновом режиме"""
    page = MainPage(backdrop_testing_driver)
    page.btn_my_lab.click()
    time.sleep(2)
    page.fild_email.click()
    page.fild_email.send_keys(negativ_email)
    clicable = not page.btn_enter.is_clickable
    assert clicable is False


@pytest.mark.parametrize("negativ_email", [generate_string(10), generate_string(255)])
def test_not_valid_my_lab(backdrop_testing_driver, negativ_email):
    """ Негативный тест авторизации пользователя c  не валидными данными.
     При вводе не валидных данных кнопка "Войти" не активная
     Запуск осуществляется в фоновом режиме"""
    page = MainPage(backdrop_testing_driver)
    page.btn_my_lab.click()
    time.sleep(2)
    page.fild_email.click()
    page.fild_email.send_keys(negativ_email)
    clicable = not page.btn_enter.is_clickable
    assert clicable is False


def test_auth_no_valid_code(testing_driver):
    """ Авторизация пользователя c не валидным кодом скидки """
    page = MainPage(testing_driver)
    page.btn_my_lab.click()
    time.sleep(2)
    page.fild_email.click()
    page.fild_email.send_keys(valid_email)
    page.btn_enter.click()
    time.sleep(2)
    page.email_pod.find()
    my_email = page.email_pod.get_attribute('value')

    assert my_email == valid_email

    page.input_code_email.click()
    page.input_code_email.send_keys(no_valid_code)
    page.button_assert_and_enter.click()
    message = page.message_no_code.find()
    print(message.text)
    assert message.text == "Введенного кода не существует"



