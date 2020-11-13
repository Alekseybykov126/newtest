from .page import *
from .test_case_1_1 import case_1_1
from .test_case_1_2 import case_1_2
from .test_case_1_3 import case_1_3

class Test:
    def setup(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--incognito')
        self.driver = webdriver.Chrome(options=options)
        #self.driver = webdriver.Chrome('C:/Users/abykov.RUTUBE/Desktop/newtest/chromedriver.exe')
        self.driver.get("https://www.matchtv.ru/")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.full_screen = 0
        self.page = MainPage(self.driver)
        self.result = ResultPage(self.driver)
        self.prof = Profile(self.driver)
        self.admin = Admin(self.driver)
        self.card = CardFilm(self.driver)

    # def teardown(self):
    #     self.driver.quit()


    def test_case_1_1(self):
        case_1_1(self, 0)

    def test_case_1_2(self):
        case_1_2(self, 0)

    def test_case_1_3(self):
        case_1_3(self, 0)
