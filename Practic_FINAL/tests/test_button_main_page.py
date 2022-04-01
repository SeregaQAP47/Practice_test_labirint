import time

from pages.main_page import MainPage
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


'''Тест основных кнопок гланой страницы'''


def test_btn_pending(testing_driver):
    """Проверка перехода на страницу "Отложено" """
    page = MainPage(testing_driver)
    page.btn_pending.click()

    assert page.get_current_url() == 'https://www.labirint.ru/cabinet/putorder/'


def test_btn_books(testing_driver):
    """Проверка перехода на страницу "Книги" """
    page = MainPage(testing_driver)
    page.btn_books.click()

    assert page.get_current_url() == 'https://www.labirint.ru/books/'


def test_best_2022(testing_driver):
    """Проверка перехода на страницу "Главное 2022" """
    page = MainPage(testing_driver)
    page.btn_best_2022.click()

    assert page.get_current_url() == 'https://www.labirint.ru/best/'


def test_btn_school(testing_driver):
    """Проверка перехода на страницу "Школа" """
    page = MainPage(testing_driver)
    page.btn_school.click()

    assert page.get_current_url() == 'https://www.labirint.ru/school/'


def test_btn_toys(testing_driver):
    """Проверка перехода на страницу "Игрушки" """
    page = MainPage(testing_driver)
    page.btn_toys.click()

    assert page.get_current_url() == 'https://www.labirint.ru/games/'


def test_btn_office_supplies(testing_driver):
    """Проверка перехода на страницу "Канцтовары" """
    page = MainPage(testing_driver)
    page.btn_office.click()

    assert page.get_current_url() == 'https://www.labirint.ru/office/'


def test_delivery_and_payment(testing_driver):
    """Проверка перехода на страницу "Доставка и оплата" """
    page = MainPage(testing_driver)
    page.btn_delivery.click()

    assert page.get_current_url() == 'https://www.labirint.ru/help/'


def test_btn_certificates(testing_driver):
    """Проверка перехода на страницу "Сертификаты" """
    page = MainPage(testing_driver)
    page.btn_certificates.click()

    assert page.get_current_url() == 'https://www.labirint.ru/top/certificates/'


def test_btn_ratings(testing_driver):
    """Проверка перехода на страницу "Рейтинги" """
    page = MainPage(testing_driver)
    page.btn_rating.click()

    assert page.get_current_url() == 'https://www.labirint.ru/rating/?id_genre=-1&nrd=1'


def test_btn_novelty(testing_driver):
    """Проверка перехода на страницу "Новинки" """
    page = MainPage(testing_driver)
    page.btn_novelty.click()

    assert page.get_current_url() == 'https://www.labirint.ru/novelty/'


def test_btn_contact(testing_driver):
    """Проверка перехода на страницу "Контакты" """
    page = MainPage(testing_driver)
    page.btn_contact.click()

    assert page.get_current_url() == 'https://www.labirint.ru/contact/'


def test_btn_support(testing_driver):
    """Проверка перехода на страницу "Поддержка" """
    page = MainPage(testing_driver)
    page.btn_support.click()

    assert page.get_current_url() == 'https://www.labirint.ru/support/'


def test_btn_pick_up_point(testing_driver):
    """Проверка перехода на страницу "Пункты самовывоза" """
    page = MainPage(testing_driver)
    page.btn_maps.click()

    assert page.get_current_url() == 'https://www.labirint.ru/maps/'


def test_btn_sale(testing_driver):
    """Проверка перехода на страницу "Скидки" """
    page = MainPage(testing_driver)
    page.btn_sale.click()

    assert page.get_current_url() == 'https://www.labirint.ru/search/?discount=1&available=1&order=actd&way=back&paperbooks=1&ebooks=1&otherbooks=1'


def test_btn_club(testing_driver):
    """Проверка перехода на страницу "Клуб" """
    page = MainPage(testing_driver)
    page.btn_club.click()

    assert page.get_current_url() == 'https://www.labirint.ru/club/'


def test_btn_geolock(testing_driver):
    """Проверка смены "Местоположение" """
    page = MainPage(testing_driver)
    page.btn_geolock.click()
    page.input_city.click()
    page.input_city.send_keys("Санкт-Петербург")
    page.input_city.send_keys(Keys.ENTER)

    title = page.city_title.get_attribute('title')
    print(title)
    assert title == "Санкт-Петербург"


def test_transition_in_social_network_vk(testing_driver):
    """ Переход на страницу ВК лабиринт """
    page = MainPage(testing_driver)
    ter = page.social_network.find()
    ActionChains(testing_driver).move_to_element(ter).perform()
    page.vk_link.click()
    time.sleep(3)
    testing_driver.switch_to.window(testing_driver.window_handles[1])
    time.sleep(5)
    assert page.get_current_url() == "https://vk.com/labirint_ru"


def test_transition_in_network_youtube(testing_driver):
    """ Переход на страницу YouTube лабиринт """
    page = MainPage(testing_driver)
    variable = page.social_network.find()
    ActionChains(testing_driver).move_to_element(variable).perform()

    page.youtube.click()
    time.sleep(3)
    testing_driver.switch_to.window(testing_driver.window_handles[1])
    time.sleep(5)
    assert page.get_current_url() == "https://www.youtube.com/user/labirintruTV"


def test_transition_in_network_odnoclass(testing_driver):
    """ Переход на страницу Одноклассники лабиринт """
    page = MainPage(testing_driver)
    variable = page.social_network.find()
    ActionChains(testing_driver).move_to_element(variable).perform()

    page.odnoclass.click()
    time.sleep(3)
    testing_driver.switch_to.window(testing_driver.window_handles[1])
    time.sleep(5)
    assert page.get_current_url() == "https://ok.ru/labirintru"


def test_transition_in_social_network_vk_child(testing_driver):
    """ Переход на страницу ВК дети лабиринт """
    page = MainPage(testing_driver)
    variable = page.social_network.find()
    ActionChains(testing_driver).move_to_element(variable).perform()

    page.vk_child.click()
    time.sleep(3)
    testing_driver.switch_to.window(testing_driver.window_handles[1])
    time.sleep(5)
    assert page.get_current_url() == "https://vk.com/labirintdeti"


def test_transition_in_zen_yandex(testing_driver):
    """ Переход на страницу Яндекс Дзен лабиринт """
    page = MainPage(testing_driver)
    variable = page.social_network.find()
    ActionChains(testing_driver).move_to_element(variable).perform()

    page.zen_ya.click()
    time.sleep(3)
    testing_driver.switch_to.window(testing_driver.window_handles[1])
    time.sleep(5)
    assert page.get_current_url() == "https://zen.yandex.ru/labirintru"


def test_transition_in_telegram(testing_driver):
    """ Переход на страницу Телеграм канала лабиринт """
    page = MainPage(testing_driver)
    variable = page.social_network.find()
    ActionChains(testing_driver).move_to_element(variable).perform()

    page.telega.click()
    time.sleep(3)
    testing_driver.switch_to.window(testing_driver.window_handles[1])
    time.sleep(5)
    assert page.get_current_url() == "https://t.me/labirintru"


def test_transition_in_tiktok(testing_driver):
    """ Переход на страницу tiktok лабиринт """
    page = MainPage(testing_driver)
    variable = page.social_network.find()
    ActionChains(testing_driver).move_to_element(variable).perform()

    page.tiktok_lab.click()
    time.sleep(3)
    testing_driver.switch_to.window(testing_driver.window_handles[1])
    time.sleep(5)
    assert page.get_current_url() == "https://www.tiktok.com/@labirintru"


def test_button_else_cd_dvd(testing_driver):
    """ Проверка кнопки еще, пореход во вкладку "СD/DVD" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_else.find()
    ActionChains(testing_driver).move_to_element(variable).perform()

    page.cd_dvd.click()
    assert page.get_current_url() == "https://www.labirint.ru/multimedia/"


def test_button_else_souvenirs(testing_driver):
    """ Проверка кнопки еще, пореход во вкладку "Сувениры" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_else.find()
    ActionChains(testing_driver).move_to_element(variable).perform()

    page.souvenirs.click()
    assert page.get_current_url() == "https://www.labirint.ru/souvenir/"


def test_button_else_magazines(testing_driver):
    """ Проверка кнопки еще, пореход во вкладку "Журналы" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_else.find()
    ActionChains(testing_driver).move_to_element(variable).perform()

    page.magazines.click()
    assert page.get_current_url() == "https://www.labirint.ru/journals/"


def test_button_else_household_goods(testing_driver):
    """ Проверка кнопки еще, пореход во вкладку "Товары для дома" из выпадающего списка"""
    page = MainPage(testing_driver)
    variable = page.btn_else.find()
    ActionChains(testing_driver).move_to_element(variable).perform()

    page.household.click()
    assert page.get_current_url() == "https://www.labirint.ru/household/"


def test_button_more_books_sale(testing_driver):
    """ Проверка кнопки "Больше книг со скидкой" """
    page = MainPage(testing_driver)
    page.more_books_sale.scroll_to_element()
    page.more_books_sale.click()
    assert page.get_current_url() == "https://www.labirint.ru/best/sale/"


def test_user_agreement(testing_driver):
    """ Проверка кнопки "18+"(Пользовательское соглашение) """
    page = MainPage(testing_driver)
    page.agreement.click()
    assert page.get_current_url() == "https://www.labirint.ru/agreement/"


def test_btn_recommendations(testing_driver):
    """Проверка кнопки "Что читать? Рекомендуем" """
    page = MainPage(testing_driver)
    page.btn_recom.click()

    assert page.get_current_url() == 'https://www.labirint.ru/now/'


