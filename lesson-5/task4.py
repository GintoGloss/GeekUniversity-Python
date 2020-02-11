# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. При этом английские
# числительные должны заменяться на русские. Новый блок строк должен записываться в новый текстовый файл.


translator = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

with open('my_old_file.txt', encoding='utf-8') as f_in:
    with open('my_new_file.txt', 'w', encoding='utf-8') as f_out:
        while True:
            next_line = f_in.readline()
            if next_line == '':
                break
            word = next_line.split()[0]
            f_out.write(next_line.replace(word, translator[word]))
