from requests import Session
import requests

url = 'https://mgupp.ru/cabinet/?login=yes'

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.1.895 Yowser/2.5 Safari/537.36"
}

datas = {
    'USER_LOGIN': '94316',
    'USER_PASSWORD': '3053060'
}

def auth_as_url(session: Session):
    cookies = {
    '_ym_uid': '1669381564886884320',
    '_ym_d': '1669381564',
    '_ga': 'GA1.2.720700097.1669381565',
    'BX_USER_ID': 'd83711b9177044b17914a6292d14852c',
    '_fbp': 'fb.1.1669901796310.1029254255',
    '_gid': 'GA1.2.582917179.1681151492',
    '_ym_isad': '1',
    'BITRIX_CONVERSION_CONTEXT_s1': '%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1681592340%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D',
    'PHPSESSID': 'RuNzVll3uZuprKxqwS8FkW1CJ7D3Ewgs',
    'BITRIX_SM_PK': 'page',
    'sputnik_session': '1681578419392|0',
    }

    headers = {
        'authority': 'mgupp.ru',
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'ru,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/x-www-form-urlencoded',
        # 'cookie': '_ym_uid=1669381564886884320; _ym_d=1669381564; _ga=GA1.2.720700097.1669381565; BX_USER_ID=d83711b9177044b17914a6292d14852c; _fbp=fb.1.1669901796310.1029254255; _gid=GA1.2.582917179.1681151492; _ym_isad=1; BITRIX_CONVERSION_CONTEXT_s1=%7B%22ID%22%3A1%2C%22EXPIRE%22%3A1681592340%2C%22UNIQUE%22%3A%5B%22conversion_visit_day%22%5D%7D; PHPSESSID=RuNzVll3uZuprKxqwS8FkW1CJ7D3Ewgs; BITRIX_SM_PK=page; sputnik_session=1681578419392|0',
        'origin': 'https://mgupp.ru',
        'referer': 'https://mgupp.ru/cabinet/?login=yes',
        'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "YaBrowser";v="23"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
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
        ('USER_LOGIN', '94316'),
        ('USER_PASSWORD', '3053060'),
        ('Login', 'Войти'),
    ]

    response = session.post('https://mgupp.ru/cabinet/', params=params, cookies=cookies, headers=headers, data=data)
    with open('data.html', 'w', encoding='utf-8') as f:
        f.write(response.text)

def main(base_url):
    s = Session()
    s.headers.update(headers)

    response = s.get(base_url, data=datas)
    #r = s.get('https://mgupp.ru/cabinet/lc_schedule/index.php', headers=headers, data=datas)


    with open('data.html', 'w', encoding='utf-8') as f:
        f.write(response.text)


if __name__=='__main__':
    auth_as_url()