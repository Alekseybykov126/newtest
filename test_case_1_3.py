from .page import *

def case_1_3(self, full_screen):

    self.page.loger('\n Запуск Тест кейс № 1_3 tvweb_new-1_3: Проверка наличия коэффициентов фонбет на главной \n')
    time.sleep(2)

    self.page.loger('Шаг 1. Скролл до блока "Ближайшие матчи"')
    target = self.driver.find_element_by_xpath('.//div[@class="heading heading-3 caption__heading"]')  # скролл до блока Ближайшие матчи
    target.location_once_scrolled_into_view

    self.page.loger('Шаг 2. Проверка наличия коэффициентов в блоке "Ближайшие матчи"')
    num_koef = len(self.driver.find_elements_by_xpath('.//div[@class="fonbet_koef"]'))
    print('Количество коэффициентов ' + str(num_koef))

    if num_koef < 2:
        assert False
        self.page.loger('Коэффициентов слишком мало, меньше 2')

    self.page.loger('Наличие коэффициентов фонбет в блоке "Ближайшие матчи" подтверждено')
    time.sleep(1)

    self.page.loger('Шаг 3. Скролл до блока "Результаты"')
    target = self.driver.find_element_by_xpath('.//div[@class="ext-widget__title"]')  # скролл до блока Результаты
    target.location_once_scrolled_into_view  # скролл
    time.sleep(1)

    self.page.loger('Шаг 4. Проверка, что активна вкладка "Сегодня"')
    self.driver.find_element_by_xpath('.//a[@class="ext-widget-statistics__day ext-widget-statistics__day_active"][contains(., "Сегодня")]')
    self.page.loger('Вкладка "Сегодня" активна')
    time.sleep(2)

    self.page.loger('Шаг 5. Проверка наличия коэффициентов в блоке "Результаты"')
    resic = str(self.result.find_link("div", "ext-widget-statistics__tables"))
    assert ('fonbet_koef') in resic
    self.page.loger('Наличие коэффициентов в блоке "Результаты" подтверждено')

    self.driver.quit()





