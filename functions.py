## functions модуль для импорта функций для работы

def func2(n):
    """Функция 2"""
# Номера телефонов находятся в столбике 'phone_number'
def clean_phone_number(phone_number):
    return ''.join(filter(str.isdigit, str(phone_number)))

# Применяем функцию к столбику с номерами телефонов
df['cleaned_phone_number'] = df['phone_number'].apply(clean_phone_number)

# Сохраняем результат в новый файл .xlsx
df.to_excel(output_file, index=False)