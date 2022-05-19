import requests

YATOKEN = ''  # место для ввода Токена


def create_folder(folder_name: str):
    headers = {'Authorization': 'OAuth ' + YATOKEN}
    params = {'path': '/' + folder_name}
    response = requests.put('https://cloud-api.yandex.net:443/v1/disk/resources', params=params, headers=headers)
    return response


def check_folder(folder_name: str):
    headers = {'Authorization': 'OAuth ' + YATOKEN}
    params = {'path': '/' + folder_name}
    response = requests.get('https://cloud-api.yandex.net:443/v1/disk/resources', params=params, headers=headers)
    return response


if __name__ == '__main__':
    print(create_folder('TestFolder'))
    print(check_folder('TestFolder'))

