from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://9gag.com/trending')
first_mem = driver.find_element(By.CLASS_NAME, 'badge-evt')
first_mem_url = first_mem.get_attribute('href')

with open('mem.txt', 'w') as mem_file:
    mem_file.write(first_mem_url)