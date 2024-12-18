import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



""" Проверка таблицы всех питомцев в разделе "Мои питомцы",
с добавлением явного ожидания элементов страницы  """
@pytest.fixture(autouse=True)
def driver():

    driver = webdriver.Chrome()
    driver.get('https://petfriends.skillfactory.ru/login')

    yield driver
    driver.quit()

def test_show_my_pets(driver):
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'email')))
    driver.find_element(By.ID, 'email').send_keys('11')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.ID, 'pass')))
    driver.find_element(By.ID, 'pass').send_keys('11')
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, 'button[type="submit"]')))
    driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.XPATH, '//[@id="navbarNav"]/ul/li[1]/a')))
    driver.find_element(By.XPATH, '//[@id="navbarNav"]/ul/li[1]/a').click()
    assert driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').text == 'Мои питомцы'
    driver.save_screenshot('allMyPets.png')


""" Проверка таблицы всех питомцев в разделе "Мои питомцы",
с добавлением неявного ожидания элементов страницы  """

def test_implicitly_wait_my_pets(driver):
    driver.implicitly_wait(5)
    driver.find_element(By.ID, 'email').send_keys('11')
    driver.find_element(By.ID, 'password').send_keys('11')
    driver.find_element(By.CSS_SELECTOR, 'button[type=submit]').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == "PetFriends"
    driver.implicitly_wait(5)
    driver.find_element(By.XPATH, '//*[@id="navbarNav"]/ul/li[1]/a').click()
    assert driver.find_element(By.XPATH,'//*[@id="navbarNav"]/ul/li[1]/a').text == 'Мои питомцы'

    images = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-img-top')
    names = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-title')
    descriptions = driver.find_elements(By.CSS_SELECTOR, '.card-deck .card-text')

    for i in range(len(names)):
        assert images[i].get_attribute('src') != ''
        assert names[i].text != ''
        assert descriptions[i].text != ''
        assert ', ' in descriptions[i]
        parts = descriptions[i].text.split(", ")
        assert len(parts[0]) > 0
        assert len(parts[1]) > 0