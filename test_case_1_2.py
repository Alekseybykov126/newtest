from .page import *

def case_1_2(self, fullscreen):

    self.page.loger("\n Запуск Тест кейс № 1_2 tvweb_new-1_1: проверка работы поиска \n")
    time.sleep(2)

    word = 'Локомотив'

    self.page.loger('Шаг 1. Клик по иконке поиска')
    self.driver.find_element_by_xpath('.//button[@class="reset-button header-slim-section__search-button"]').click()
    time.sleep(2)

    self.page.loger('Шаг 2. Ввод слова в строку поиска: ' + word)
    self.driver.find_element_by_xpath('.//input[@class="search-bar__input"]').send_keys(word)
    time.sleep(1)

    self.page.loger('Шаг 3. Клик поиск')
    self.driver.find_element_by_xpath('.//button[@class="reset-button search-bar__button-submit"]').click()
    time.sleep(3)

    self.page.loger('Шаг 4. Получение слова на странице:')
    StringText = self.driver.find_element_by_xpath('.//strong[@class="search-keyword-match"]')
    StringText = StringText.get_attribute('innerHTML')
    self.page.loger(StringText)

    self.page.loger('Шаг 5. Сравнение слова из поиска со словом на странице')
    if word == StringText:
        self.page.loger('Поиск работает')
    else:
        assert 'Поиск не работает!'


    self.driver.quit()