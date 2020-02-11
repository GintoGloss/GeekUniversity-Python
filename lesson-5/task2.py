# 2. Создать текстовый файл (не программно), сохранить в нем несколько строк, выполнить подсчет количества строк,
# количества слов в каждой строке.


with open('my_file.txt') as f:
    lines = f.readlines()
print('Строк:', len(lines))
for count, line in enumerate(lines):
    print('Слов в строке №{}: {}'.format(count, len(line.split())))
