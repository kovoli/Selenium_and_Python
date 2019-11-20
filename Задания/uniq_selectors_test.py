from selenium import webdriver
import time

try:
    link = "http://suninjuly.github.io/registration1.html"
    link_with_bag = 'http://suninjuly.github.io/registration2.html'
    browser = webdriver.Firefox()
    browser.get(link_with_bag)

    first_name = browser.find_element_by_css_selector('.first_block input.first')
    first_name.send_keys('"Мой ответ"')
    last_name = browser.find_element_by_css_selector('.first_block input.second')
    last_name.send_keys("Мой ответ")
    email = browser.find_element_by_css_selector('.first_block input.third')
    email.send_keys("Мой ответ")

    # fields = browser.find_elements_by_css_selector('input[required]')
    # for i in fields:
    #   i.send_keys("Мой ответ")

    time.sleep(5)
    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

    # находим элемент, содержащий текст
    welcome_text_elt = browser.find_element_by_tag_name("h1")
    # записываем в переменную welcome_text текст из элемента welcome_text_elt
    welcome_text = welcome_text_elt.text

    # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()