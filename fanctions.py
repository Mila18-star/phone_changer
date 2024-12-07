## модуль для импорта функций 


import pandas as pd
def func1(n):
    """Функция 1"""
input_file = "phone_numbers.xlsx"  # Указали путь к файлу
output_file = "cleaned_phones.xlsx"      # Выходной файл

# Считали данные из Excel файла
df = pd.read_excel(input_file)