from selenium import webdriver
import time, math

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Firefox()
    browser.get(link)

    find_text = str(math.ceil(math.pow(math.pi, math.e)*10000))

    link_to_click = browser.find_element_by_link_text(find_text)
    link_to_click.click()

    # А если хотим найти элемент со ссылкой по подстроке, то нужно написать следующий код:
    #
    # link = browser.find_element_by_partial_link_text("examples")
    # link.click()

    input1 = browser.find_element_by_tag_name('input')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_class_name('city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
