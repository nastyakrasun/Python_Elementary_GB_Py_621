# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
my_str = input('Введите строку из слов, разделённых пробелами: ')
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
print('\nВывод каждого слова с новой строки с нумерацией строк')
my_list = (my_str.split())
n = 1
i = 0
while i < int(len(my_list)):
    elem = my_list[i]
    # Если в слово длинное, выводить только первые 10 букв в слове.
    print(n, elem[:10])
    n += 1
    i += 1