from selenium import webdriver
import time, os

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

try:
    browser = webdriver.Firefox()
    link = "http://suninjuly.github.io/file_input.html"
    browser.get(link)

    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'text.txt')

    for i in ['firstname', 'lastname', 'email']:
        browser.find_element_by_css_selector(f"input[name='{i}']").send_keys('Meine Daten')
        time.sleep(0.5)

    input_file = browser.find_element_by_id('file')
    input_file.send_keys(file_path)

    button = browser.find_element_by_css_selector('button.btn')
    button.click()

finally:
    time.sleep(5)
    browser.quit()
