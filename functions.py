## functions модуль для импорта функций для работы

# TODO import <зависимость из задания>


def func1(n):
    """Функция 1"""
    pass


def clean_phone_number(phone_number):
    """Функция 2"""
    # Номера телефонов находятся в столбике 'phone_number'
    return ''.join(filter(str.isdigit, str(phone_number)))

def apply_changes(path, output_file):
    df = func1(path)

    # Применяем функцию к столбику с номерами телефонов
    df['cleaned_phone_number'] = df['phone_number'].apply(clean_phone_number)

    # Сохраняем результат в новый файл .xlsx
    df.to_excel(output_file, index=False)