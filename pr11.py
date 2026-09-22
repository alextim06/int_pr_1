import re
import datetime

class Date:
    def __init__(self, dd=0, mm=0, yyyy=0):
        self.dd = dd
        self.mm = mm
        self.yyyy = yyyy

class Patient:
    def __init__(self):
        self.passport = ""
        self.name = ""
        self.birth_date = Date()
        self.phone = ""
        self.temperature = 0.0
        self.skin_color = (0, 0, 0)   # RGB


def input_passport():
    while True:
        p = input("Введите паспорт 11 11-111111: ").strip()
        if re.match(r'^\d{2}\s\d{2}-\d{6}$', p):
            return p
        print("Ошибка! Не корректные данные")

def input_name():
    while True:
        n = input("Введите Имя: ").strip()
        return n

def input_birth_date():
    while True:
        d = input("Введите дату рождения yyyy-mm-dd: ").strip()
        m = re.match(r'^(\d{4})-(\d{2})-(\d{2})$', d)
        if m:
            yyyy, mm, dd = map(int, m.groups())
            try:
                datetime.date(yyyy, mm, dd)
                return dd, mm, yyyy
            except:
                print("Ошибка! Несуществующая дата")
                continue
        print("Ошибка! Не корректные данные")

def input_phone():
    while True:
        p = input("Введите телефон +7(999) 999-99-99 или 8(999) 999-9999: ").strip()
        if re.match(r'^\+\d\(\d{3}\)\s\d{3}-\d{2}-\d{2}$', p) or re.match(r'^\d\(\d{3}\)\s\d{3}-\d{4}$', p):
            return p
        print("Ошибка! Не корректные данные")

def input_temperature():
    while True:
        t = input("Введите температуру XX.XX: ").strip()
        try:
            temp = float(t)
            if 30.0 <= temp <= 45.0:
                return temp
            print("Ошибка! Диапазон: 30 - 45")
        except:
            print("Ошибка! Не корректные данные")

def input_skin_color():
    while True:
        c = input("Введите цвет кожи в формате R,G,B (например 255,200,150): ").strip()
        m = re.match(r'^(\d{1,3})\s*,\s*(\d{1,3})\s*,\s*(\d{1,3})$', c)
        if m:
            r, g, b = map(int, m.groups())
            if 0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255:
                return (r, g, b)
            print("Ошибка! Каждое значение должно быть от 0 до 255")
        else:
            print("Ошибка! Не корректные данные")

def ask():
    patient = Patient()

    patient.passport = input_passport()

    patient.name = input_name()

    dd, mm, yyyy = input_birth_date()
    patient.birth_date = Date(dd, mm, yyyy)

    patient.phone = input_phone()

    patient.temperature = input_temperature()

    patient.skin_color = input_skin_color()

    patient_list.append(patient)

def show(patient):

    print("ДАННЫЕ О ПАЦИЕНТЕ")
    print(f"Паспорт: {patient.passport}")
    print(f"ФИО: {patient.name}")
    print(f"Дата рождения: {patient.birth_date.yyyy:04d}-{patient.birth_date.mm:02d}-{patient.birth_date.dd:02d}")
    print(f"Телефон: {patient.phone}")
    print(f"Температура: {patient.temperature:.2f}")
    print(f"Цвет кожи (RGB): {patient.skin_color[0]}, {patient.skin_color[1]}, {patient.skin_color[2]}")


def main():
    global patient_list
    patient_list = []
    while True:
        print("Хотите заполнить данные пациента? (Y/N)")
        answer = input()
        if answer == "Y" or answer == "y":
            ask()
        elif answer == "N" or answer == "n":
            for p in patient_list:
                show(p)
            break
        else:
            print("Ошибка! Не корректный ввод")

main()