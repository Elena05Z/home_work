from selenium import webdriver
from selenium.webdriver.common.by import By

def check_elements():
    driver = webdriver.Chrome()
    
    try:
        driver.get("https://www.saucedemo.com")
        
        
        username_field = driver.find_element(By.ID, 'user-name')
        password_field = driver.find_element(By.ID, 'password')
        submit_button = driver.find_element(By.ID, 'login-button')
        
        if all([username_field, password_field, submit_button]):
            print('Элементы найдены')
            
    except Exception as e:
        print(f'Ошибка: {e}')
    finally:
        driver.quit()


check_elements()
