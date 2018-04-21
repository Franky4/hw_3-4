import tokens  # мой файл где хранятся токены
import requests

AUTH_URL = "https://oauth.yandex.ru/authorize"

# APP_ID = "" вынесено во внешний файл tokens
APP_ID = tokens.APP_ID

auth_data = {
    'response_type': 'token',
    'client_id': APP_ID
}

# print('?'.join((AUTH_URL, urlencode(auth_data))))
# TOKEN ='' вынесено во внешний файл tokens

TOKEN = tokens.TOKEN


class YaMetrikaUser:
    def __init__(self, token):
        self.token = token

    def get_counter_list(self):
        params = {
            'oauth_token': self.token
        }
        response = requests.get('https://api-metrika.yandex.ru/management/v1/counters', params)
        return [c['id'] for c in response.json()['counters']]

    def get_counter_stat(self, idc):
        params = {
            'oauth_token': self.token,
            'id': idc,
            'metrics': 'ym:s:visits,ym:s:pageviews,ym:s:users'
        }
        response = requests.get('https://api-metrika.yandex.ru/stat/v1/data', params)
        return response.json()['totals']


user1 = YaMetrikaUser(TOKEN)
print('Список ваших счетчиков: {}'.format(user1.get_counter_list()))
my_stat = user1.get_counter_stat('45843831')
print('Визитов {}, Просмотров {}, Посетителей {}'.format(*my_stat))

