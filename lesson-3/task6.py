# 6. Реализовать функцию int_func(), принимающую слово из маленьких латинских букв и возвращающую его же,
# но с прописной первой буквой. Например, print(int_func(‘text’)) -> Text. Продолжить работу над заданием. В
# программу должна попадать строка из слов, разделенных пробелом. Каждое слово состоит из латинских букв в нижнем
# регистре. Сделать вывод исходной строки, но каждое слово должно начинаться с заглавной буквы. Необходимо
# использовать написанную ранее функцию int_func().


def int_func(word):
    """Принимает слово в нижнем регистре. Возвращает слово с прописной первой буквой"""
    try:
        word = str(word)
    except ValueError:
        return None
    if word.islower() and word.isalpha():
        return word.title()
    return None


old_string = input("Введите строку из слов, написанных в нижнем регистре: ")
new_string = ""
try:
    for index, word in enumerate(old_string.split(), start=1):
        new_string += int_func(word)
        if index < len(old_string.split()):
            new_string += " "
except TypeError:
    print("Неправильная строка")
else:
    print(new_string)
