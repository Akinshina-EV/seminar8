import csv
import find_employee as fe
import view as v

def menu():
    while True:
        print('\nДобро пожаловать в базу данных (БД)\n'
              '"ООО Ромашка".\n'
              '\nВыберете пункт меню:\n'
              '\n1 - Показать все записи в БД.\n'
              '2 - Найти запись.\n'
              '3 - Закрыть БД.\n')
        number_menu = input('Введите порядковый номер пункта меню: ')

        if number_menu.isdigit() and int(number_menu) in range(1, 4):
            if int(number_menu) == 1:
                bd = []
                with open('Phonebook.csv', 'r', newline='') as csv_file:
                    reader = csv.reader(csv_file)
                    for row in reader:
                        v.show_contact(row)
            if int(number_menu) == 2:
                fined = input('Введите ключевое слово для поиска: ')
                fe.search(fined)
                v.show_contact(row)
            if int(number_menu) == 3:
                print('До свиданья!')
        else:
            print(
                '\nТакого пункта меню не существует.\n'
                'Введите цифру, соответствующую пункту меню.')
