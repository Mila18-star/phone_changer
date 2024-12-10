## functions модуль для импорта функций для работы

import pandas as pd

def read_data(n):    
    """Функция 1"""
    input_file = "phone_numbers.xlsx"  # Указали путь к файлу
    output_file = "cleaned_phones.xlsx"      # Выходной файл

    # Считали данные из Excel файла
    return pd.read_excel(input_file)

def clean_phone_number(phone_number):
    """Функция 2"""
    # Номера телефонов находятся в столбике 'phone_number'
    return ''.join(filter(str.isdigit, str(phone_number)))

def apply_changes(path, output_file):
    df = read_data(path)

    # Применяем функцию к столбику с номерами телефонов
    df['cleaned_phone_number'] = df['phone_number'].apply(clean_phone_number)

    # Сохраняем результат в новый файл .xlsx
    df.to_excel(output_file, index=False)
 


 