## модуль для импорта функций 


import pandas as pd

def read_data(n):    
    """Функция 1"""
    input_file = "phone_numbers.xlsx"  # Указали путь к файлу
    output_file = "cleaned_phones.xlsx"      # Выходной файл

    # Считали данные из Excel файла
    return pd.read_excel(input_file)