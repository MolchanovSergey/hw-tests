from main import create_folder, check_folder


class TestMain:

    def test_success_create_folder(self):
        print('\n' + 'Проверка на успешное создание папки')
        assert create_folder('TestFolder').status_code == 201

    def test_success_check_folder(self):
        print('\n' + 'Проверка на поиск папки')
        assert check_folder('TestFolder').status_code == 200

    def test_failed_create_folder(self):
        print('\n' + 'Проверка на некорректное создание папки')
        assert create_folder('').status_code == 409

    def test_failed_check_folder(self):
        print('\n' + 'Проверка на поиск несущестрвующей папки')
        assert check_folder('InvalidFolder').status_code == 404