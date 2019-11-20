from selenium import webdriver
import time, os


#browser = webdriver.Firefox()
#link = "https://SunInJuly.github.io/execute_script.html"
#browser.get(link)

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))


current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'text.txt')