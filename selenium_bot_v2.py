from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


# Запуск браузера Edge
driver = webdriver.Edge()

try:
    driver.get("https://9gag.com/trending")

    wait = WebDriverWait(driver, 20)

    # Ждём появления кнопки Accert в DOM
    try:
        accept_btn = wait.until(
            EC.presence_of_element_located(
                (By.XPATH, "//button[@title='Accept' or normalize-space()='Accept']")
            )
        )

        # Кликаем по кнопке через JS
        driver.execute_script("arguments[0].click();", accept_btn)
        print("Кнопка Accept нажата")

    except TimeoutException:
        print("Баннер не появился")    

    # Теперь ищем мемы
    mem = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.badge-evt'))
    )
    
    url = mem.get_attribute("href")

    with open('mem2.txt', 'w', encoding="utf-8") as mem_file:
        mem_file.write(url)
finally:
    # Закрываем браузер в любом случае
    driver.quit()        