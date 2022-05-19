documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]
directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}


def people(documents, user_number):

    """Поиск владельца документа по номеру"""

    for document in documents:
        if document["number"] == user_number:
            print(f'\nДокумент пренадлежит:')
            result = document["name"]
            return result
    result = f'\nДокумент с номером: {user_number} не зарегестрирован'
    return result



def get_directori(directories, user_number):
    """Определение номера картотеки по номеру документа"""
    for num_box in directories:
        if user_number in directories[num_box]:
            print(f'\nДокумент расположен в картотеке №')
            result = num_box
            return result
    result = f'\nДокумент с номером {user_number} нет в картотеках '
    return result


def get_list_docs(list_docs):
    """Вывод данных имеющихся документов"""
    result = []
    for doc in documents:
        result.append(doc['type'] + ' "' + doc['number'] + '"' + ' "' + doc['name']+ '"')
    return result



def add_doc(doc_type, doc_number, doc_owner, direct_number):
    """Добавление нового документа"""
    for keys in directories.keys():
        if direct_number in directories:
            documents.append({"type": doc_type, "number": doc_number, "name": doc_owner})
            directories[direct_number].append(doc_number)
    else:
        print('Ошибка! Укажите корректный номер полки')


def main():
    while True:
        user_cmd = input('\nВведите команду:')
        if user_cmd == 'p':
            user_number = input('\nВведите номер документа: \n')
            print(people(documents, user_number))
        elif user_cmd == 's':
            user_number = input('\nВведите номер документа: ')
            print(get_directori(directories, user_number))
        elif user_cmd == 'l':
            for i in get_list_docs(documents):
                print(i)
        elif user_cmd == 'a':
            add_doc(input('Введите тип документа:'), input('Введите номер документа:'), input('Введите ФИО владельца:'),
                    input('Введите номер полки:'))
        elif user_cmd == 'q':
            print('Выход из программы')
            break
        else:
            print('\nтакой команды нет в списке.')





if __name__ == '__main__':
   main()