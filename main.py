## main стартовый модуль проекта
#project 4

from functions import apply_changes
 
# инициализационный скрипт
if __name__=="__main__":
    input_file = "phone_numbers.xlsx"
    output_file = "cleaned_phones.xlsx"  
    apply_changes(input_file, output_file)  # Передаем необходимые аргументы

     
  
