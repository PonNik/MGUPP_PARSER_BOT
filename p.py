from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from bs4 import BeautifulSoup as bs


async def parce():
    options = webdriver.EdgeOptions()
    options.add_argument('--headless')

    # Инициализируем драйвер браузера
    driver = webdriver.ChromiumEdge(options=options)

    # Переходим на страницу авторизации
    driver.get('https://mgupp.ru/cabinet/?login=yes')

    # Заполняем форму логина и пароля
    login_input = driver.find_element(by=By.NAME, value='USER_LOGIN')
    login_input.send_keys('94316')
    password_input = driver.find_element(by=By.NAME, value='USER_PASSWORD')
    password_input.send_keys('3053060')

    # Нажимаем кнопку "Войти"
    submit_button = driver.find_element(by=By.CSS_SELECTOR , value='input[type="submit"]')
    submit_button.click()

    # Переходим на нужную страницу
    driver.get('https://mgupp.ru/cabinet/lc_schedule/index.php')

    try:
        all_data = WebDriverWait(driver, 10).until(lambda x: x.find_element(By.CLASS_NAME, 'cd-schedule__events'))
        print("Page is ready!")

        
        all_data_html = all_data.get_attribute('innerHTML')
        soup = bs(all_data_html, "html.parser")
        
        less = []
        itog = []

        days = soup.find_all('li')
        for day in days:
            text = {}
            try:
                day_text = day.find('div', 'cd-schedule__top-info _dayWeek top-info-fon').find('span').text
                lessons = day.find_all('li', 'cd-schedule__event')
            except:
                lessons.extend(day.find_all('li', 'cd-schedule__event'))

            for lesson in lessons:
                if less != [[]]:
                    info_lesson = '({start} - {end}) {name} {audit}\n\n'.format(name=lesson.find('a').get('_disc'), 
                                                                            start=lesson.find('a').get('data-start'), 
                                                                            end=lesson.find('a').get('data-end'),
                                                                            audit=lesson.find('a').get('_auditoria'))
                    less.append(info_lesson)
            if less != []:
                text['day'] = day_text
                text['lessons'] = less
                
                
                lessons = []
                less = []
            if text != {}:
                itog.append(text)
        driver.quit()
        return itog
    except TimeoutException:
        print("Loading took too much time!")
        
        # Закрываем браузер
        driver.quit()
        return 'EROR'