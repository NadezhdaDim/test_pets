import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def driver():
    driver = webdriver.Chrome(executable_path='C:\chomedriver\chomedriver.exe')
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver
    driver.quit()


def test_show_all_pets(driver):
    driver.find_element(By.ID,'email').send_keys('11')
    driver.find_element(By.ID,'password').send_keys('11')
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    assert driver.find_element(By.TAG_NAME,'h1').text == "PetFriends"


def test_all_my_pets(driver):
    driver.find_element(By.ID,'email').send_keys('11')
    driver.find_element(By.ID,'password').send_keys('11')
    driver.find_element(By.CSS_SELECTOR,'button[type=submit').click()
    assert driver.find_element(By.TAG_NAME,'h1').text == "PetFriends"
    time.sleep(1)
    driver.find_element(By.XPATH,'//a[text()="Мои питомцы"]').click()

    pets_number = driver.find_element(By.XPATH,'//div[@class=".col-sum-4 left"]').text.split('\n')[1].split(': ')[1]
    pets_count = driver.find_elements(By.XPATH,'//table[@class="table table-hover"]/tbody/tr')

    assert int(pets_number) == len(pets_count)


def test_pets_photo(driver):
    driver.find_element(By.ID, 'email').send_keys('11')
    driver.find_element(By.ID, 'password').send_keys('11')
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    time.sleep(1)
    driver.find_element(By.XPATH, '//a[text()="Мои питомцы"]').click()

    images = driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR,'.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0