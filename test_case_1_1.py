from .page import *

def case_1_1(self, fullscreen):

    #self.page.loger("\n Запуск Тест кейс № 1_1 tvweb_new-1_1: авторизация \n")
    print("\n Запуск Тест кейс № 1_1 tvweb_new-1_1: авторизация \n")
    time.sleep(2)

    self.page.login_matchtv('9776410337', 'Alekseybykov126')
    self.page.loger('Авторизация прошла успешно')

    resic = str(self.result.find_link("a", "reset-link pm-gate__button"))
    assert ('Выход') in resic
    self.page.loger('Кнопка "Вход" сменилась на "Выход"')

    self.page.loger('Шаг 5. Клик по иконке пользователя')
    self.driver.find_element_by_xpath('.//a[@href="/profile"]').click()
    time.sleep(2)

    self.driver.find_element_by_xpath('.//h3[@class="profile-header__item heading heading-3"]')
    self.page.loger('Осуществлён переход в личный кабинет')
    time.sleep(1)

    self.page.loger('Шаг 6. Клик по кнопке "Выход"')
    self.driver.find_element_by_xpath('.//a[@href="/pm/logout"]').click()
    time.sleep(1)

    self.driver.find_element_by_xpath('.//div[@class="form logout-form"]')
    self.page.loger('Появилась форма "Выйти из аккаунта?"')
    time.sleep(2)

    self.page.loger('Шаг 7. Подтверждение выхода из акаунта')
    self.driver.find_element_by_xpath('.//button[@type="button"]').click()
    time.sleep(1)

    resic = str(self.result.find_link("span", "pm-gate__label"))
    assert ('Вход') in resic
    self.page.loger('Кнопка "Выход" сменилась на "Вход"')

    self.driver.quit()