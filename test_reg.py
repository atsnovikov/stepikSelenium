import unittest

class TestReg(unittest.TestCase):
    def test_reg1(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time

        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        # mandatory_elements = browser.find_elements(By.CSS_SELECTOR, "div.first_block &gt; div &gt; input")
        # for element in mandatory_elements:
        #    element.send_keys('asdfg')
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input.first")
        input1.send_keys('aaaaaaa')

        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input.second")
        input2.send_keys('bbbbbb')

        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input.third")
        input3.send_keys('ccccccc')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "не нашелся текст при регистрации во второй форме")
        browser.quit()

    def test_reg2(self):
        from selenium import webdriver
        from selenium.webdriver.common.by import By
        import time

        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        # mandatory_elements = browser.find_elements(By.CSS_SELECTOR, "div.first_block &gt; div &gt; input")
        # for element in mandatory_elements:
        #    element.send_keys('asdfg')
        input1 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.first_class input.first")
        input1.send_keys('aaaaaaa')

        input2 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.second_class input.second")
        input2.send_keys('bbbbbb')

        input3 = browser.find_element(By.CSS_SELECTOR, "div.first_block div.third_class input.third")
        input3.send_keys('ccccccc')

        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        self.assertEqual("Congratulations! You have successfully registered!", welcome_text, "не нашелся текст при регистрации во второй форме")
        browser.quit()


if __name__ == '__main__':
    unittest.main()