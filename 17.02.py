# 4. Объявите класс с именем MediaPlayer с двумя методами:
# open(file) - для открытия медиа-файла с именем file (создает локальное свойство filename со значением аргумента file в объекте класса
# MediaPlayer) play0 - для воспроизведения медиа-файла (выводит на экран строку "Воспроизведение «название медиа-файла>")
# Создайте два экземпляра этого класса с именами: media1 и media2. Вызовите из них метод ореп ( с аргументом "filemedia1" для объекта media1 и
# "filemedia2" для объекта media2. После этого вызовите через объекты метод play). При этом, на экране должно отобразиться две строки (без
# кавычек):
# "Воспроизведение filemedia1"
# "Воспроизведение filemedia2"

class MediaPlayer:
    def open(self, file):
        self.filename = file

    def play(self):
        print(f"Воспроизведение {self.filename}")

media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("filemedia1")
media2.open("filemedia2")

media1.play()
media2.play()

# 5. Объявите класс с именем Graph и методами:
# set_data(data) - передача набора данных data для последующего отображения (data - список числовых данных); draw - отображение данных (в
# том же порядке, что и в списке data)
# и атрибутом:
# LIMIT_Y = [0, 10]
# Метод set_data() должен формировать локальное свойство data объекта класса Graph. Атрибут data должен ссылаться на переданный в метод
# список. Метод draw0 должен выводить на экран список в виде строки из чисел, разделенных пробелами и принадлежащие заданному диапазону
# атрибута LIMIT_Y (границы включаются).
# Создайте объект graph_1 класса Graph, вызовите для него метод set_data( и передайте список:
# [10, -5, 100, 20, 0, 80, 45, 2, 5, 7]
# Затем, вызовите метод draw0 через объект graph_1. На экране должна появиться строка с соответствующим набором чисел, записанных через
# пробел. Например (вывод без кавычек):
# "10 02 5 7"

class Graph:
    LIMIT_Y = [0, 10]

    def set_data(self, data):
        self.data = data

    def draw(self):
        filtered_data = [str(d) for d in self.data if self.LIMIT_Y[0] <= d <= self.LIMIT_Y[1]]
        print(" ".join(filtered_data))

graph_1 = Graph()
graph_1.set_data([10, -5, 100, 20, 0, 80, 45, 2, 5, 7])
graph_1.draw()

# 7. Имеется следующий класс для считывания информации из входного потока:
# import sys
# class StreamReader:
# FIELDS = ('id', 'title', 'pages')
# def readlines(self):
# sd = StreamData()
# res = sd.create(self.FIELDS, 1st_ in)
# return sd, res
# lst_ in = list(map(str.strip, sys.stdin.readlines())) # считывание списка строк из входного потока
# Которым, затем, можно воспользоваться следующим образом:
# sr = StreamReader)
# data, result = sr. readlines()
# Необходимо перед классом StreamReader объявить еще один класс StreamData с методом:
# def create(self, fields, Ist_values): ...
# который бы на входе получал кортеж FIELDS из названий локальных атрибутов (передается в атрибут fields) и список строк Ist in (передается в атрибут Ist_values) и формировал
# бы в объекте класса StreamData локальные свойства с именами полей из fields и соответствующими значениями из Ist_values.
# Если создание локальных свойств проходит успешно, то метод create® возвращает True, иначе - False. Если число полей и число строк не совпадает, то метод create® возвращает
# False и локальные атрибуты создавать не нужно.
# P.S. В программе нужно дополнительно объявить только класс StreamData. Больше ничего делать не нужно.

import sys

class StreamData:
    def create(self, fields, lst_values):
        if len(fields) != len(lst_values):
            return False
        for field, value in zip(fields, lst_values):
            setattr(self, field, value)
        return True

class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        return sd, res

lst_in = list(map(str.strip, sys.stdin.readlines()))

sr = StreamReader()
data, result = sr.readlines()
if result:
    print(f"id: {data.id}, title: {data.title}, pages: {data.pages}")
else:
    print("Ошибка: количество полей и строк не совпадает.")

# 9. Из входного потока читаются строки данных с помощью команды:
# Ist_in - list(map(str.strip, sys.stdin.readlines())) # считывание списка строк из входного потока
# в формате: id, name, old, salary (записанные через пробел). Например:
# 1 Сергей 35 120000 2 Федор 23 12000 3 Иван 13 1200 ....
# То есть, каждая строка - это элемент списка Ist_in.
# Необходимо в класс DataBase:
# class DataBase:
# Ist_data = ll
# FIELDS = ('id', 'name', 'old', 'salary')
# добавить два метода:
# select(self, a, b) - возвращает список из элементов списка Ist _data в диапазоне [а; b] (включительно) по их индексам (не id, а индексам списка); также учесть, что граница b может
# превышать длину списка. insert(self, data) - для добавления в список Ist_data новых данных из переданного списка строк data;
# Каждая запись в списке Ist_data должна быть представлена словарем в формате:
# ('id': "номер", 'name': 'имя", 'old': 'возраст", 'salary': 'зарплата")
# Например:
# (id': "1', 'name': 'Сергей", 'old': '35', 'salary: 120000}
# Примечание: в этой задаче число элементов в строке (разделенных пробелом) всегда совпадает с числом полей в коллекции FIELDS.
# P. S. Ваша задача только добавить два метода в класс DataBase.

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def select(self, a, b):
        return self.lst_data[a:min(b + 1, len(self.lst_data))]

    def insert(self, data):
        
        for item in data:
            
            item_dict = dict(zip(self.FIELDS, item.split()))
            self.lst_data.append(item_dict)

db = DataBase()
lst_in = ['1 Сергей 35 120000', '2 Федор 23 12000', '3 Иван 13 1200']
db.insert(lst_in)
print(db.select(0, 2))

# 10. Объявите класс с именем Translator (для перевода с английского на русский) со следующими методами:
# add(self, eng, rus) - для добавления новой связки английского и русского слова (если английское слово уже существует, то новое русское слово добавляется как синоним для
# перевода, например, go - идти, ходить, ехать); если связка eng-rus уже существует, то второй раз ее добавлять не нужно, например: add('go', "идти"), add("go', 'идти"); remove(self,
# eng) - для удаления связки по указанному английскому слову, translate(self, eng) - для перевода с английского на русский (метод должен возвращать список из русских слов,
# соответствующих переводу английского слова, даже если в списке всего одно слово).
# Все добавления и удаления связок должны выполняться внутри каждого конкретного объекта класса Translator, т.е. связки хранить локально внутри экземпляров классов класса
# Translator.
# Создайте экземпляр tr класса Translator и вызовите метод add для следующих связок:
# tree - дерево
# саг - машина
# car - автомобиль
# leaf - лист
# river - река
# до - идти
# до - ехать
# до - ходить
# milk - молоко
# Затем методом remove0 удалите связку для английского слова саг. С помощью метода translate0 переведите слово до. Результат выведите на экран в виде строки из всех русских
# слов, связанных со словом до:
# Вывод в формате: идти ехать ходить

class Translator:
    def __init__(self):
        self.dictionary = {}

    def add(self, eng, rus):
        if eng in self.dictionary:
            if rus not in self.dictionary[eng]:
                self.dictionary[eng].append(rus)
        else:
            self.dictionary[eng] = [rus]

    def remove(self, eng):
        if eng in self.dictionary:
            del self.dictionary[eng]

    def translate(self, eng):
        return self.dictionary.get(eng, [])

tr = Translator()
tr.add('tree', 'дерево')
tr.add('car', 'машина')
tr.add('car', 'автомобиль')
tr.add('leaf', 'лист')
tr.add('river', 'река')
tr.add('go', 'идти')
tr.add('go', 'ехать')
tr.add('go', 'ходить')
tr.add('milk', 'молоко')

tr.remove('car')
print(' '.join(tr.translate('go')))