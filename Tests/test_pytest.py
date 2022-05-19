import unittest
from app import people, get_directori, get_list_docs,  documents, directories


class TestMain(unittest.TestCase):

    def test_people(self):
        print('\n' + 'Проверка people')
        self.assertEqual(people(documents, '11-2'), 'Геннадий Покемонов')

    def test_get_directori(self):
        print('\n' + 'Проверка get_directori')
        self.assertEqual(get_directori(directories, '11-2'), '1')

    def get_list_docs(self):
        print('\n' + 'Проверка get_list_docs')
        self.assertIn('invoice "11-2" "Геннадий ', get_list_docs(documents))
