## functions модуль для импорта функций для работы

import pandas as pd
def func1(n):
    """Функция 1"""
input_file = "phone_numbers.xlsx"  # Указали путь к файлу
output_file = "cleaned_phones.xlsx"      # Выходной файл

# Считали данные из Excel файла
df = pd.read_excel(input_file)

def func2(n):
    """Функция 2"""
# Номера телефонов находятся в столбике 'phone_number'
def clean_phone_number(phone_number):
    return ''.join(filter(str.isdigit, str(phone_number)))

# Применяем функцию к столбику с номерами телефонов
df['cleaned_phone_number'] = df['phone_number'].apply(clean_phone_number)

# Сохраняем результат в новый файл .xlsx
df.to_excel(output_file, index=False)