import os
os.system('cls')
import codecs

# Поиск контакта
def find():
    sub_string = str(input('Введите имя и/или фамилию: '))
    with codecs.open('spravochnik.txt', 'r' , encoding='utf-8') as file:      
        for line in file:
            if sub_string.casefold() in line.casefold():
                a = line
    return(a)

# Вывод всего словаря
def show_all():
    with codecs.open('spravochnik.txt', 'r', encoding='utf-8') as file:   
        for line in file:
            print(line)

# Вспомогательная функция записи файла в словарь
def write_in_dct():
    d = {}
    with codecs.open("spravochnik.txt", 'r', encoding='utf-8') as file:
        for line in file:
            key, *value = line.split()
            key = int(key)
            d[key] = value
    return d, key


# Добавление нового контакта
def added_new_contact(d, key):
    if len(d) == 0:
        d[1] = [input('Введите Имя: '),input('Введите Фамилию: '), input('Введите Отчество: '), input('Введите Номер телефона: ')]
    else:
        count = key+1
        d[count] = [input('Введите Имя: '),input('Введите Фамилию: '), input('Введите Отчество: '), input('Введите Номер телефона: ')]
    return d


# Изменение номера контакта и поиск по ФИО
# def change_phone_number_old(d):
#     print(d)
#     name = input('Введите имя для поиска: ').casefold()
#     s_name = input('Введите фамилию для поиска: ').casefold()
#     t_name = input('Введите отчество для поиска: ').casefold()
#     for i in d:
#         st = d[i]
#         if (name == str(st[0]).casefold()) and (s_name == str(st[1]).casefold()) and (t_name == str(st[2]).casefold()):
#             st1 = ' '.join(st)
#             chose = input(f'Изменить номер телефона контакта {st1}?(Да/Нет): ').casefold()
#             if chose == 'да'.casefold():
#                 st[3] = input('Введите новый номер телефона: ')
#             d[i] = st
#     return d    

# Изменение по одному из ФИО
def change_phone_number(d):
    name = input('Введите имя для поиска: ').casefold()
    s_name = input('Введите фамилию для поиска: ').casefold()
    t_name = input('Введите отчество для поиска: ').casefold()
    for i in d:
        st = d[i]
        if (name == str(st[0]).casefold()) or (s_name == str(st[1]).casefold()) or (t_name == str(st[2]).casefold()):
            st1 = ' '.join(st)
            chose = input(f'Изменить номер телефона контакта {st1}?(Да/Нет): ').casefold()
            if chose == 'да'.casefold():
                st[3] = input('Введите новый номер телефона: ')
            d[i] = st
    return d    

# Изменение ФИО
def change_contact_in_sprv(d):
    name = input('Введите имя для поиска: ').casefold()
    s_name = input('Введите фамилию для поиска: ').casefold()
    t_name = input('Введите отчество для поиска: ').casefold()
    for i in d:
        st = d[i]
        if (name == str(st[0]).casefold()) or (s_name == str(st[1]).casefold()) or (t_name == str(st[2]).casefold()):
            st1 = ' '.join(st)
            if input(f'Изменить данные контакта {st1}(Да/Нет)?: ').casefold() == 'да'.casefold():
                chose = input(f'Изменить Имя контакта {st1}?(Да/Нет): ').casefold()
                if chose == 'да'.casefold():
                    st[0] = input('Введите новое имя: ')
                chose = input(f'Изменить Фамилию контакта {st1}?(Да/Нет): ').casefold()
                if chose == 'да'.casefold():
                    st[1] = input('Введите новую Фамилию: ')
                chose = input(f'Изменить Отчество контакта {st1}?(Да/Нет): ').casefold()
                if chose == 'да'.casefold():
                    st[2] = input('Введите новое Отчество: ')
                d[i] = st
    return d    

# Конструкция удаления
def delete_contact(d):
    name = input('Введите имя для поиска: ').casefold()
    s_name = input('Введите фамилию для поиска: ').casefold()
    t_name = input('Введите отчество для поиска: ').casefold()
    for i in d:
        st = d[i]
        if (name == str(st[0]).casefold()) or (s_name == str(st[1]).casefold()) or (t_name == str(st[2]).casefold()):
            st1 = ' '.join(st)
            if input(f'удалить контакт {st1}(Да/Нет)?: ').casefold() == 'да'.casefold():
                    count = i
    d.pop(count)
    lengt = int(len(d))
    if count != lengt+1:
        for j in range(1, lengt+1):
            if (len(d)+1) > j > (count - 1):
                d[j] = d[j+1]
                last1 = j
        d.pop(last1+1)  
        dct1 = dict(sorted(d.items()))
    return dct1

    
# Конструкция записи в файл
def write_in_file(d):
    with codecs.open("spravochnik.txt", 'w', encoding='utf-8') as file:
                
        for i in d:
            if i != 1:
                file.writelines('\n')
            a = d[i]
            b = None
            i = str(i)
            b = i +" " + " ".join(a)
            file.writelines(b)
        return b

# Полная отчиска справочника
def delete_all():
    open("spravochnik.txt", 'w', encoding='utf-8')
    return None

# Главное меню
def main_menu(command):
    if command == 'Найти'.casefold():
        print(find())
    elif command == 'Показать'.casefold():
        show_all()
    elif command == 'Добавить'.casefold():
        write_in_file(added_new_contact(write_in_dct()[0],write_in_dct()[1]))
    elif command == 'Изменить'.casefold():
        write_in_file(change_phone_number(write_in_dct()[0]))
    elif command == 'Переименовать'.casefold():
        write_in_file(change_contact_in_sprv(write_in_dct()[0]))
    elif command == 'Удалить'.casefold():
        write_in_file(delete_contact(write_in_dct()[0]))
    elif command == 'Стереть'.casefold():
        delete_all()
    else:
        print('Ничего не исполнено')


# Основной блок
 
print('info: выберите что хотите сделать:\n1. Найти контакт "Найти"\n2. Добавить контакт команда "Добавить",\n3. Показать весь справочник "Показать"')
print('4. Изменить номер контакта "Изменить"\n5. Переименовать контакт "Переименовать"\n6. Удалить контакт "Удалить"\n7. Очистить весь справочник "Стереть"')
command = input('Введите команду из списка выше: ').casefold()
main_menu(command)