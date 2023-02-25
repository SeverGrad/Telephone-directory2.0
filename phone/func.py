import sqlite3


# Регистрация контакат
def registrationContact():
    last_name = input('Введите фамилию: ').lower()
    first_name = input('Введите имя: ').lower()
    phone = input('Введите личный номер телефона: ')
    phone_job =  input('Введите рабочий номер телефона: ')
    email =  input('Введите электронную почту: ')

    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        
        values = [last_name, first_name, phone, phone_job, email]
        cursor.execute("INSERT INTO phone(last_name, first_name, phone, phone_job, email) VALUES(?, ?, ?, ?, ?)", values)
        db.commit()
        print('Вы зарегестрировали новый контакт!')
    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()

# Главное меню
def main_menu():
    main_menu = '''/nКоманды справочника:
    1 - поиск телефона по фамилии:
    2 - поиск почты по фамилии:
    3 - поиск фамилии по телефону:
    4 - редактирование контакта:
    5 - регистрация контакта:
    0 - выход
    '''
    print(main_menu)

# меню изменения
def menu_update():
    menu_update = '''/nКоманды справочника редактирование:
    1 - изменение телефона по id:
    2 - изменение email по id:
    3 - отчистка графы телефон:
    4 - отчистка графа email:
    5 - удаление по id:
    0 - назад
    '''
    print(menu_update)


# Изменение телефона по id
# редактирование по фамилии
def update_numberPhones_by_id():
    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        text = input('Введите фамилию для поиска: ').lower()
        record = cursor.execute("SELECT id, last_name, first_name, phone FROM phone WHERE last_name = ?", (text, ))
        record = cursor.fetchall()
        print("Всего строк:", (len(record)))
        print('Вывод каждой строки')
        for row in record:
            print("id",(row[0]))
            print("Фамилия:", (row[1]))
            print("Имя", (row[2]))
            print("Телефон", (row[3]), end="\n\n")
        search_id = input('Выберите и введите id для изменения номера телефона: ')
        new_phone = input('Введите номер телефона: ')
        update_phones = "UPDATE phone SET phone = ? where id = ? "
        
        data = (new_phone, search_id)
        cursor.execute(update_phones, data)
        db.commit()
        print('Запись обновлена')
        

    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()


# Изменение email по id
def update_email_by_id():
    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        text = input('Введите фамилию для поиска: ').lower()
        record = cursor.execute("SELECT id, last_name, first_name, email FROM phone WHERE last_name = ?", (text, ))
        record = cursor.fetchall()
        print("Всего строк:", (len(record)))
        print('Вывод каждой строки')
        for row in record:
            print("id",(row[0]))
            print("Фамилия:", (row[1]))
            print("Имя", (row[2]))
            print("email", (row[3]), end="\n\n")
        search_id = input('Выберите и введите id для изменения email: ')
        new_email = input('Введите новый email: ')
        update_phones = "UPDATE phone SET email = ? where id = ? "
        data = (new_email, search_id)
        cursor.execute(update_phones, data)
        db.commit()
        print('Запись обновлена')
        

    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()        



# удаление графа телефон
def delete_numberPhones_by_id():
    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        text = input('Введите фамилию для поиска: ').lower()
        record = cursor.execute("SELECT id, last_name, first_name, phone FROM phone WHERE last_name = ?", (text, ))
        record = cursor.fetchall()
        print("Всего строк:", (len(record)))
        print('Вывод каждой строки')
        for row in record:
            print("id",(row[0]))
            print("Фамилия:", (row[1]))
            print("Имя", (row[2]))
            print("Телефон", (row[3]), end="\n\n")
        search_id = input('Выберите и введите id для изменения номера телефона: ')
        update_phones = "UPDATE phone SET phone = NULL where id = ? "
        cursor.execute(update_phones, search_id)
        db.commit()
        print('Запись обновлена')
    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()


# удаление email
def delete_email_by_id():
    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        text = input('Введите фамилию для поиска: ').lower()
        record = cursor.execute("SELECT id, last_name, first_name, email FROM phone WHERE last_name = ?", (text, ))
        record = cursor.fetchall()
        print("Всего строк:", (len(record)))
        print('Вывод каждой строки')
        for row in record:
            print("id",(row[0]))
            print("Фамилия:", (row[1]))
            print("Имя", (row[2]))
            print("email", (row[3]), end="\n\n")
        search_id = input('Выберите и введите id для изменения email: ')
        update_phones = "UPDATE phone SET email = NULL where id = ? "
        cursor.execute(update_phones, search_id)
        db.commit()
        print('Запись обновлена')
    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()



# поиск телефона по фамилии

def search_phone():
    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        text = input('Введите фамилию для поиска: ').lower()
        cursor.execute("SELECT id, last_name, first_name, phone, phone_job FROM phone WHERE last_name = ?", (text, ))
        record = cursor.fetchall()
        print("Всего строк:", (len(record)))
        print('Вывод каждой строки')
        for row in record:
            print("id",(row[0]))
            print("Фамилия:", (row[1]))
            print("Имя", (row[2]))
            print("Телефон", (row[3]))
            print("Рабочий телефон", (row[4]), end="\n\n")
        db.commit()
    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()
    return

# поиск фамилии по телефону

def search_first_name():
    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        text = input('Введите номер телефона для поиска: ')
        cursor.execute("SELECT id, last_name, first_name, phone FROM phone WHERE phone = ?", (text, ))
        record = cursor.fetchall()
        print("Всего строк:", (len(record)))
        print('Вывод каждой строки')
        for row in record:
            print("id",(row[0]))
            print("Фамилия:", (row[1]))
            print("Имя", (row[2]))
            print("Телефон", (row[3]), end="\n\n")
        db.commit()
        print(cursor.fetchall())
    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()
    return

# поиск почты по фамилии

def search_email():
    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        text = input('Введите фамилию для поиска: ').lower()
        cursor.execute("SELECT id, last_name, first_name, email FROM phone WHERE last_name = ?", (text, ))
        record = cursor.fetchall()
        print("Всего строк:", (len(record)))
        print('Вывод каждой строки')
        for row in record:
            print("id",(row[0]))
            print("Фамилия:", (row[1]))
            print("Имя", (row[2]))
            print("email", (row[3]), end="\n\n")
        db.commit()
        print(cursor.fetchall())
        

    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()








# Удаление контакта версия 2
def delete_contact_by_id2():
    try:
        db = sqlite3.connect("phones.db")
        cursor = db.cursor()
        text = input('Введите фамилию для поиска: ').lower()
        record = cursor.execute("SELECT id, last_name, first_name FROM phone WHERE last_name = ?", (text, ))
        record = cursor.fetchall()
        print("Всего строк:", (len(record)))
        print('Вывод каждой строки')
        for row in record:
            print("id",(row[0]))
            print("Фамилия:", (row[1]))
            print("Имя", (row[2]), end="\n\n")
        delete_by_id = input('Выберети и введите нужный id для удаления: ')
        cursor.execute("DELETE from phone where id = ? ", (delete_by_id))
        print('Контакт удален')
        db.commit()
    except sqlite3.Error as e:
        print('Error ', e)
    finally:
        cursor.close()
        db.close()
    return
        