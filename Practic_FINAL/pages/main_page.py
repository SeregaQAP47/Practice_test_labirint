from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'https://www.labirint.ru/'
        super().__init__(web_driver, url)


    # auth кнопка "Мой Лаб"
    btn_my_lab = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.top-link-main_cabinet.js-b-autofade-wrap[href="#"]')
    # Поле для ввода авторизации(первичное)
    fild_email = WebElement(css_selector='.new-auth__full-input.full-input.js-full-input.js-autofocus.js-input-email .full-input__input.formvalidate-error')
    # Строка email после ввода
    email_pod = WebElement(css_selector='.js-new-form.js-auth-email-sent.auth-header__module.auth-header__module_show input[name="email"]')
    # Кнопка входа для авторизации (первичная)
    btn_enter = WebElement(id='g-recap-0-btn')
    # Поле ввода кода скидки для авторизации
    input_code_email = WebElement(css_selector='.full-input__input.formvalidate-error[type="text"]')
    # Кнопка проверить и войти
    button_assert_and_enter = WebElement(xpath='//*[@id="auth-email-sent"]/input[5]')

    btn_my_lab_cabinet = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.top-link-main_cabinet.js-b-autofade-wrap')
    # Кнопка "Мои данные и насторойки"
    btn_my_data_and_options = WebElement(css_selector='.cabinet-menu__link[href="/cabinet/personal/"]')
    # Поле email person
    data_email = WebElement(css_selector='.page-contact-info--input.b-form-input-m-verifiable.b-form-input.readonly.email-input-personal.iforms')

    # Пользовательское соглашение
    agreement = WebElement(css_selector='.b-header-e-icon-adult.b-header-e-icon-adult-m-big.b-header-e-sprite-background[href="/agreement/"]')

    # Поле поиск
    input_search = WebElement(id='search-field')
    # Кнопка поиск
    btn_search = WebElement(css_selector='.b-header-b-search-e-btntxt')

    products_titles_king= ManyWebElements(css_selector='.products-row[data-title="Поиск: Стивен Кинг"]')
    products_titles = ManyWebElements(xpath='// *[ @ id = "rubric-tab"] / div[3] / div[1] / div[3] / div[1]')

    # Кнопка фильтра "В наличии"
    btn_filter_presence = WebElement(xpath='//*[@id="catalog-navigation"]/form[1]/div[1]/div[2]/div[1]/div[1]/a[3]/div[1]')
    # Кнопка "отложено"
    btn_pending = WebElement(xpath='// span[contains(text(), "Отложено")]')
    # Кнопка "Еще"
    btn_else = WebElement(xpath='//span[contains(text(),"Еще")]')
    # Пункт CD/DVD выпадающего списка кнопки "Ещё"
    cd_dvd = WebElement(xpath='//a[@title="Аудиокниги, музыка, видеофильмы, компьютерные программы, игры и др."]')
    # Пункт "Сувениры" выпадающего списка кнопки "Ещё"
    souvenirs = WebElement(xpath='//a[@title="Сувениры, альбомы для фотографий, фоторамки, календари."]')
    # Пункт "Журналы" выпадающего списка кнопки "Ещё"
    magazines = WebElement(xpath='//a[@title="Литературные журналы: художественные и публицистические, поэтические."]')
    # Пункт "Товары для дома" выпадающего списка кнопки "Ещё"
    household = WebElement(xpath='//a[@title="Товары для дома"]')

    # Кнопка "Книги"
    btn_books = WebElement(css_selector='.b-header-b-menu-e-text[href="/books/"]')
    # Кнопка "Главное 2022"
    btn_best_2022 = WebElement(css_selector='.b-header-b-menu-e-text[href="/best/"]')
    # Кнопка "Школа"
    btn_school = WebElement(css_selector='.b-header-b-menu-e-text[href="/school/"]')
    # Кнопка "Игрушки"
    btn_toys = WebElement(css_selector='.b-header-b-menu-e-text[href="/games/"]')
    # Кнопка "Канцтовары"
    btn_office = WebElement(css_selector='.b-header-b-menu-e-text[href="/office/"]')

    # Кнопка "Доставка и оплата"
    btn_delivery = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/help/"]')
    # Кнопка "Сертификаты"
    btn_certificates = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/top/certificates/"]')
    # Кнопка "Рейтинги"
    btn_rating = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/rating/?id_genre=-1&amp;nrd=1"]')
    # Кнопка "Новинки"
    btn_novelty = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/novelty/"]')
    # Кнопка "Контакты"
    btn_contact = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/contact/"]')
    # Кнопка "Что читать? Рекомендуем"
    btn_recom = WebElement(css_selector='.b-header-labelaction-text.b-header-b-logo-e-discount-e-text-m-long')
    # Кнопка "Поддержка"
    btn_support = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/support/"]')
    # Кнопка "1990 Пунктов самовывоза"
    btn_maps = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/maps/"]')
    # Кнопка "Скидки"
    btn_sale = WebElement(css_selector='.b-header-b-sec-menu-e-link[href="/sale/"]')
    # Кнопка "Клуб"
    btn_club = WebElement(css_selector='.b-header-b-menu-e-text[href="/club/"]')
    # Кнопка "выбора города"
    btn_geolock = WebElement(css_selector='.b-header-b-menu-e-text.js-header-menu-region-name')
    # Строка выбора города
    input_city = WebElement(id='region-post')
    city_title = WebElement(css_selector='.region-location-icon-txt')

    # элемент "В соцсетях"
    social_network = WebElement(css_selector='.b-header-b-sec-menu-e-link.b-labirint-all-social-network.have-dropdown-touchlink[data-stype="href"]')
    # vk лабиринт
    vk_link = WebElement(css_selector='.b-header-b-social-e-icon-link.w25p.analytics-click-js[href="https://vk.com/labirint_ru"]')
    # youtube лабиринт
    youtube = WebElement(css_selector='.b-header-b-social-e-icon-link.w25p.analytics-click-js[href="https://www.youtube.com/user/labirintruTV"]')
    # однокласники
    odnoclass = WebElement(css_selectro='.b-header-b-social-e-icon-link.w25p.analytics-click-js[href="https://ok.ru/labirintru"]')
    # labirintdeti
    vk_child = WebElement(css_selectro='.b-header-b-social-e-icon-link.w25p.analytics-click-js[href="https://vk.com/labirintdeti"]')
    # zen.yandex.ru labirint
    zen_ya = WebElement(css_selectro='.b-header-b-social-e-icon-link.w25p.analytics-click-js[href="https://zen.yandex.ru/labirintru"]')
    # телеграм
    telega = WebElement(css_selectro='.b-header-b-social-e-icon-link.w25p.analytics-click-js[href="https://t.me/labirintru"]')
    # tiktok.com labirintru
    tiktok_lab = WebElement(css_selectro='.b-header-b-social-e-icon-link.w25p.analytics-click-js[href="https://www.tiktok.com/@labirintru"]')

    btn_to_cart = WebElement(id='buy819919')

    btn_ofform_close = WebElement(css_selector='.b-basket-popinfo-close[href="javascript:void(0);"]')
    cart_btn = WebElement(css_selector='.b-header-b-personal-e-link.top-link-main.analytics-click-js.cart-icon-js[href="/cart/"]')
    book_vedmak_cart = WebElement(css_selector = '.cover[href="/books/819919/"]')

    # Книга "Ведьмак,меч предназначения"
    book_vedmak = ManyWebElements(xpath='//div[@class="card-column card-column_gutter col-xs-6 col-sm-3 col-md-1-5 col-xl-2"]/div[@data-product-id="819919"]')

    # Фото у всех книг на странице по запросу поиска "Ведьмак"
    images_all_book_vedmak = ManyWebElements(css_selector='div.products-row img.book-img-cover')

    # Название книги у всех книг на странице по запросу поиска "Ведьмак"
    name_all_book_vedmak = ManyWebElements(css_selector='div.products-row .product.need-watch.watched .product-title')

    # множественный поиск элементов по запросу "Ведьмак"
    all_price_vedmak = ManyWebElements(css_selector='div.products-row .product.need-watch.watched')
    # Кнопка "Больше книг со скидкой"
    more_books_sale = WebElement(css_selector='.btn.btn-not-avaliable.autodiscounts__btn.autodiscounts__padding[href="/best/sale/"]')
    # Сообщение "Введенного кода не существует"
    message_no_code = WebElement(xpath='//small[contains(text(),"Введенного кода не существует")]')

    # Кнопка убрать в отложено
    like_defer = WebElement(css_selector='.icon-fave.track-tooltip.js-open-deferred-block[data-id_book="751513"]')
    # кнопка поиск
    btn_search_two = WebElement(css_selector='.b-header-b-search-e-btn')
    # в корзину
    basket = WebElement(css_selector='.btn.buy-link.btn-primary[data-idtov="751513"]')
    # python book
    python_book = WebElement(css_selector='.product.need-watch.watched[data-product-id="751513"]')
    # Книга в отложеном
    book_python_pending = WebElement(css_selector='.product.need-watch.product_labeled.product-cart.watched[data-product-id="751513"]')
    # кнопка лайк в отложеном (для того чтобы убрать из "отложено" для прохождения повторных тестов)
    like_button = WebElement(css_selector='.icon-fave.track-tooltip.js-open-deferred-block.js-deferred-remove.hovering[data-id_book="751513"]')
