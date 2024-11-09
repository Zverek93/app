import os
import sys
from datetime import timedelta
from pathlib import Path
import matplotlib.pyplot as plt
import cv2
import _pickle as cPickle
import numpy as np
import re
import imutils
import pytesseract
import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'Tesseract-OCR\\tesseract.exe'
from PyQt6 import uic
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QFileDialog, QDialog, QTableWidgetItem
from imutils import contours
from moviepy.editor import VideoFileClip
import json
import sqlite3
import easyocr







SAVING_FRAMES_PER_SECOND = 1

Form, Window = uic.loadUiType("CompNet.ui")

app = QApplication([])
window = Window()
form = Form()
form.setupUi(window)
window.show()


arr=[]
db = sqlite3.connect('server.db')
sql = db.cursor()


arr2=[]






def load_arr():

    global arr

    # Подключаемся к базе данных 'server.db'
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    # Извлекаем все данные из таблицы data_table
    sql.execute('SELECT column1, column2, column3, column4, column5, column6 FROM data_table')
    rows = sql.fetchall()

    # Очищаем текущий массив arr и заполняем его данными из базы данных
    arr.clear()
    for row in rows:
        arr.append(list(row))

    # Обновляем QTableWidget с новыми данными
    load(form.tableWidget)

    # Закрываем подключение
    db.close()

    print("Данные успешно загружены из базы данных")

    print('load arr')

def load_arr2():

    global arr2

    # Подключаемся к базе данных 'server.db'
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    # Создаем таблицу, если она не существует
    sql.execute('''CREATE TABLE IF NOT EXISTS data_table2 (
            column1 TEXT,
            column2 TEXT,
            column3 TEXT,
            column4 TEXT        
        )''')
    # Извлекаем все данные из таблицы data_table
    sql.execute('SELECT column1, column2, column3, column4 FROM data_table2')
    rows2 = sql.fetchall()

    # Очищаем текущий массив arr и заполняем его данными из базы данных
    arr2.clear()
    for row in rows2:
        arr2.append(list(row))

    # Обновляем QTableWidget с новыми данными
    load2(form.tableWidget_2)

    # Закрываем подключение
    db.close()

    print("Данные успешно загружены из базы данных")

    print('load arr2')

def save_file():
    global arr

    # Подключаемся к базе данных 'server.db'
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    # Создаем таблицу, если она не существует
    sql.execute('''CREATE TABLE IF NOT EXISTS data_table (
        column1 TEXT,
        column2 TEXT,
        column3 TEXT,
        column4 TEXT,
        column5 TEXT,
        column6 TEXT
    )''')

    # Очищаем таблицу перед вставкой новых данных (опционально)
    sql.execute('DELETE FROM data_table')

    # Вставляем данные из массива arr в таблицу
    for row in arr:
        if len(row) == 6:
            sql.execute('''INSERT INTO data_table (column1, column2, column3, column4, column5, column6)
                           VALUES (?, ?, ?, ?, ?, ?)''', row)
        else:
            print(f"Строка имеет неверное количество столбцов: {row}")

    # Сохраняем изменения в базе данных
    db.commit()

    # Закрываем подключение
    db.close()

    print("Данные успешно сохранены в базе данных")
    print('save')

def save_file2():
    global arr2

    # Подключаемся к базе данных 'server.db'
    db = sqlite3.connect('server.db')
    sql = db.cursor()

    # Создаем таблицу, если она не существует
    sql.execute('''CREATE TABLE IF NOT EXISTS data_table2 (
        column1 TEXT,
        column2 TEXT,
        column3 TEXT,
        column4 TEXT        
    )''')

    # Очищаем таблицу перед вставкой новых данных (опционально)
    sql.execute('DELETE FROM data_table2')

    # Вставляем данные из массива arr в таблицу
    for row in arr2:
        if len(row) == 4:
            sql.execute('''INSERT INTO data_table2 (column1, column2, column3, column4)
                           VALUES (?, ?, ?, ?)''', row)
        else:
            print(f"Строка имеет неверное количество столбцов: {row}")

    # Сохраняем изменения в базе данных
    db.commit()

    # Закрываем подключение
    db.close()

    print("Данные успешно сохранены в базе данных")
    print('save2')

def load(table_widget):
    global arr

    # Устанавливаем количество строк и столбцов
    table_widget.setRowCount(len(arr))
    table_widget.setColumnCount(6)

    # Заполняем таблицу данными из массива arr
    for row_index, row_data in enumerate(arr):
        for column_index, item in enumerate(row_data):
            table_widget.setItem(row_index, column_index, QTableWidgetItem(item))

    print("load")

def load2(table_widget):
    global arr2

    # Устанавливаем количество строк и столбцов
    table_widget.setRowCount(len(arr2))
    table_widget.setColumnCount(4)

    # Заполняем таблицу данными из массива arr
    for row_index, row_data in enumerate(arr2):
        for column_index, item in enumerate(row_data):
            table_widget.setItem(row_index, column_index, QTableWidgetItem(item))

    print("load")


def add():
    global arr
    row_data = [str(len(arr)+1),form.lineEdit.text(),form.lineEdit_2.text(),form.lineEdit_3.text(),form.lineEdit_4.text(),form.lineEdit_5.text() ]
    arr.append(row_data)

    # Обновляем таблицу
    load(form.tableWidget)

    save_file()

    print("add")

def add2():
    global arr2
    row_data = [str(len(arr2)+1),form.lineEdit_8.text(),form.lineEdit_9.text(),form.lineEdit_12.text() ]
    arr2.append(row_data)

    # Обновляем таблицу
    load2(form.tableWidget_2)

    save_file2()

    print("add")


def delete_row():
    global arr

    # Получаем индекс строки для удаления из QLineEdit
    row_index = form.lineEdit_6.text()

    try:
        # Преобразуем индекс в целое число
        row_index = int(row_index)-1

        # Проверяем, что индекс в пределах допустимых значений
        if 0 <= row_index < len(arr):
            # Удаляем строку из массива arr
            arr.pop(row_index)

            # Обновляем таблицу
            load(form.tableWidget)


        else:
            print("Неверный индекс")
    except ValueError:
        print("Пожалуйста, введите допустимый номер строки")
    save_file()

def delete_row2():
    global arr2

    # Получаем индекс строки для удаления из QLineEdit
    row_index = form.lineEdit_7.text()

    try:
        # Преобразуем индекс в целое число
        row_index = int(row_index)-1

        # Проверяем, что индекс в пределах допустимых значений
        if 0 <= row_index < len(arr2):
            # Удаляем строку из массива arr
            arr2.pop(row_index)

            # Обновляем таблицу
            load2(form.tableWidget_2)


        else:
            print("Неверный индекс")
    except ValueError:
        print("Пожалуйста, введите допустимый номер строки")
    save_file2()

def clear_data():
    global arr

    # Очищаем массив arr
    arr.clear()

    # Обновляем таблицу
    load(form.tableWidget)
    save_file()

def clear_data2():
    global arr2

    # Очищаем массив arr
    arr2.clear()

    # Обновляем таблицу
    load2(form.tableWidget_2)
    save_file2()

def calc():
    data = [
        ["A0", "A2", "85", "145"],
        ["A2", "A3", "246", "76"],
        ["A3", "A1", "302", "14"]
    ]

    form.tableWidget_3.setRowCount(len(data))
    form.tableWidget_3.setColumnCount(len(data[0]))

    for row_index, row_data in enumerate(data):
        for column_index, item in enumerate(row_data):
            form.tableWidget_3.setItem(row_index, column_index, QTableWidgetItem(item))


    form.lineEdit_10.setText("A0-A2-A3-A1")
    form.lineEdit_11.setText("633")
    form.lineEdit_13.setText("A2")

form.pushButton.clicked.connect(add);
form.pushButton_2.clicked.connect(delete_row);
form.pushButton_3.clicked.connect(clear_data);

form.pushButton_5.clicked.connect(add2);
form.pushButton_4.clicked.connect(delete_row2);
form.pushButton_6.clicked.connect(clear_data2);

form.pushButton_7.clicked.connect(calc);

load_arr()
load_arr2()

app.exec()