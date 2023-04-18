from requests import Session
import datetime
import os
import json

from dotenv import load_dotenv
from bs4 import BeautifulSoup as bs


load_dotenv()
LOGIN_URL = os.getenv('LOGIN_URL')
LOGIN = os.getenv('LOGIN')
PASSWORD = os.getenv('PASSWORD')

def auth_as_url(session: Session):
    headers = {
        'authority': 'mgupp.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru,en;q=0.9',
        'cache-control': 'max-age=0',
        'origin': 'https://mgupp.ru',
        'referer': LOGIN_URL,
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.1.895 Yowser/2.5 Safari/537.36',
    }

    params = {
        'login': 'yes',
    }

    data = [
        ('AUTH_FORM', 'Y'),
        ('TYPE', 'AUTH'),
        ('backurl', '/cabinet/'),
        ('Login', 'Войти'),
        ('USER_LOGIN', LOGIN),
        ('USER_PASSWORD', PASSWORD),
        ('Login', 'Войти'),
    ]

    response = session.post('https://mgupp.ru/cabinet/', 
                            params=params, 
                            headers=headers, 
                            data=data)

# getting group id
def Get_Group_Guids(session: Session):
    json_data = {
        'FLCode': LOGIN,
    }

    response = session.post(
        'https://api.cloud.mgupp.ru/api-mgupp-kubernetes/EISGroupRoute/GetGroupGuidsForLKByFlCode',
        json=json_data,
    ).json()
    return response['data']['GroupGuid']

def get_Raspisanie_Kalendar(session: Session, group_guids):
    # getting dates beginning and end of the week
    today = datetime.datetime.today()
    monday = today - datetime.timedelta(datetime.datetime.weekday(today))
    sunday = today + datetime.timedelta(6 - datetime.datetime.weekday(today))

    data = {
        'DateList': '{monday}, {tuesday}, {wednesday}, {thursday}, {friday}, {saturday}, {sunday}'.format(
        monday=monday.strftime('%Y.%m.%d'),
        tuesday=(monday + datetime.timedelta(days=1)).strftime('%Y.%m.%d'),
        wednesday=(monday + datetime.timedelta(days=2)).strftime('%Y.%m.%d'),
        thursday=(monday + datetime.timedelta(days=3)).strftime('%Y.%m.%d'),
        friday=(monday + datetime.timedelta(days=4)).strftime('%Y.%m.%d'),
        saturday=(monday + datetime.timedelta(days=5)).strftime('%Y.%m.%d'),
        sunday=sunday.strftime('%Y.%m.%d')),
        'FlCode': LOGIN,
        'Roles[0][Role]': 'Student',
        'GroupGuid': group_guids,
        'DateS': monday.date().strftime('%d.%m.%Y'),
        'DateF': sunday.date().strftime('%d.%m.%Y'),
    }

    response = session.post(
        'https://mgupp.ru/cabinet/lc_schedule/GetRaspisanie-kalendar.php',
        data=data,
    )

    days_list = []

    soup = bs(response.text, 'html.parser')

    days = soup.find('div', 'cd-schedule__events')

    groups = days.find_all('li', 'cd-schedule__group')
    for group in groups:
        day = group.find('div', 'cd-schedule__top-info _dayWeek top-info-fon')
        if day is not None:
            itog = []
            data_lessons = group.find_all('li', 'cd-schedule__event')
            for data_lesson in data_lessons:
                data = data_lesson.find('a')
                itog.append({
                    'name': data.get('_disc'), 
                    'data-start': data.get('data-start'),
                    'data-end': data.get('data-end'),
                    '_auditoria': data.get('_auditoria'),
                    'data-type': data.get('data-type'),
                    '_dateoflesson': data.get('_dateoflesson'),
                             })
            days_list.append({'day': day.text.strip(), 'data_lessons': itog})
        else:
            itog = []
            data_lessons = group.find_all('li', 'cd-schedule__event')
            for data_lesson in data_lessons:
                data = data_lesson.find('a')
                itog.append({
                    'name': data.get('_disc'), 
                    'data-start': data.get('data-start'),
                    'data-end': data.get('data-end'),
                    '_auditoria': data.get('_auditoria'),
                    'data-type': data.get('data-type'),
                    '_dateoflesson': data.get('_dateoflesson'),
                            })
            days_list[-1]['data_lessons'] += itog

    with open('rasp.json', 'w', encoding='utf-8') as file:
        json.dump(days_list, file, indent=4, ensure_ascii=False)

    return days_list

def parse():
    session = Session()

    auth_as_url(session)
    group_guids = Get_Group_Guids(session)
    return get_Raspisanie_Kalendar(session, str(group_guids))    

if __name__=='__main__':
    parse()