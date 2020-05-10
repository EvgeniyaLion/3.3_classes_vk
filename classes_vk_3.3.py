from urllib.parse import urlencode
import requests
import json

# Получаем токен

# APP_ID = 7458698
# user_id = 41036009
# OAUTH_URL = 'https://oauth.vk.com/authorize'
# OAUTH_PARAMS = {
#      'client_id': APP_ID,
#      'user_id': user_id,
#      'display': 'page',
#      'scope': 'status, friends, offline',
#      'response_type': 'token',

#      'v': '5.103'
#  }

# print('?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS))))


TOKEN = "4175f8f2d38e906d39bf4153cd6465fa749c1d6ebe5b52729958ad3e69cf64785c316f17db0d51e5ff318"

# response = requests.get('https://api.vk.com/method/users.get?user_id=41036009&',
#                         params={'access_token': TOKEN, 'v': 5.103})


class User():

    def __init__(self, token, user_id):
        self.token = token
        self.id = user_id

    def __str__(self):
        return str(f'https://vk.com/id{self.id}')

    def get_id(user):
        resp = requests.get(
            'https://api.vk.com/method/friends.get',
            params={
                'access_token': TOKEN,
                'user_id': user.id,
                'v': 5.103
            }
        )
        return resp.json()['response']['items']

    def __and__(self, user):
        user_id = set(self.get_id())
        user_2_id = set(user.get_id())
        friends_list = list(user_id & user_2_id)
        print(f"Список общих друзей пользователей:\n{friends_list}")
        return friends_list


user_1 = User(TOKEN, 41036009)
user_2 = User(TOKEN, 150817306)

user_1 & user_2

print(f"\nСсылка на профиль пользователя:\n{user_1}")
