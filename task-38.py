""" Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. 
Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения 
и удаления данных  """


def writing_person():

    lastname = input("фамилия: ")
    name = input("имя: ")
    surname = input("отчество: ")
    tel = input("телефон: ")
    data = open("phonebook.txt", "a", encoding="utf-8")
    data.writelines(
        f"фамилия:{lastname} имя:{name} отчество:{surname} телефон:{tel}\n")
    data.close()


def search():

    lookfor = input("кого ищем? ")
    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            if lookfor in line:
                print(line)


def print_phonebook():

    with open("phonebook.txt", "r", encoding="utf-8") as data:
        for line in data:
            print(line)


def load():

    new_phonebook = input("введите ссылку: ")
    with open(new_phonebook, "r", encoding="utf-8") as data:
        with open("phonebook.txt", "a+", encoding="utf-8") as data_1:
            for line in data:
                if line not in data_1:
                    data_1.write(line)
            data_1.write("\n")


def update_person():

    lastname = input(
        "Введите фамилию человека, данные которого нужно изменить: ")
    name = input("Введите имя человека, данные которого нужно изменить: ")
    with open("phonebook.txt", "r+", encoding="utf-8") as data:
        lines = data.readlines()
        data.seek(0)
        for line in lines:
            if f"фамилия:{lastname} имя:{name}" not in line:
                data.write(line)
            else:
                new_lastname = input("Введите новую фамилию: ")
                new_name = input("Введите новое имя: ")
                new_surname = input("Введите новое отчество: ")
                new_tel = input("Введите новый телефон: ")
                data.write(
                    f"фамилия:{new_lastname} имя:{new_name} отчество:{new_surname} телефон:{new_tel}\n")
        data.truncate()


def delete_person():

    lastname = input(
        "Введите фамилию человека, запись о котором нужно удалить: ")
    name = input("Введите имя человека, запись о котором нужно удалить: ")
    with open("phonebook.txt", "r+", encoding="utf-8") as data:
        lines = data.readlines()
        data.seek(0)
        for line in lines:
            if f"фамилия:{lastname} имя:{name}" not in line:
                data.write(line)
        data.truncate()


print("""1 - добавление,
2 - поиск,
3 - вывод на экран,
4 - импорт из файла,
5 - изменение данных,
6 - удаление данных""")
ask = int(input())
if ask == 1:
    writing_person()
elif ask == 2:
    search()
elif ask == 3:
    print_phonebook()
elif ask == 4:
    load()
elif ask == 5:
    update_person()
elif ask == 6:
    delete_person()
else:
    print("нет такой команды")
