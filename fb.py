from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def test_facebook_login():
    # Данные для входа
    email = "a.lena.o@mail.ru"  # Необходимо указать актуальный e-mail
    password = "password"  # Необходимо указать пароль

    # Инициализация WebDriver
    driver = webdriver.Chrome()
    driver.get("https://www.facebook.com/")

    time.sleep(3)  # Подождать загрузку страницы

    # Ввод email
    email_input = driver.find_element(By.ID, "email")
    email_input.send_keys(email)

    # Ввод пароля
    password_input = driver.find_element(By.ID, "pass")
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)

    time.sleep(30)  # Ожидание загрузки

    # Проверка успешности входа
    if "facebook.com" in driver.current_url:
        print("Авторизация успешна")
    else:
        print("Ошибка авторизации")


if __name__ == "__main__":
    test_facebook_login()
