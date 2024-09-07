import time
import requests


def check_website():
    try:
        response = requests.get('https://google.com/', timeout=5)
        if response.status_code == 200:
            print('available')
        else:
            print('not available')
    except requests.ConnectionError:
        print('failed to connect')
    except requests.HTTPError:
        print('broken')
    except requests.ReadTimeout:
        print('timeout')


while True:
    check_website()
    time.sleep(30)
