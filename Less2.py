# Напишите программу, которая по данному числу N от 1 до 9 выводит на экран N пингвинов. Изображение одного пингвина
# имеет размер 5×9 символов, между двумя соседними пингвинами также имеется пустой (из пробелов) столбец. Разрешается
# вывести пустой столбец после последнего пингвина. Для упрощения рисования скопируйте пингвина из примера в среду
# разработки.
kol = int(input())
penguin1 = '   _~_     '
penguin2 = '  (o o)    '
penguin3 = ' /  V  \\   '
penguin4 = '/(  _  )\\  '
penguin5 = '  ^^ ^^    '
print(penguin1 * kol)
print(penguin2 * kol)
print(penguin3 * kol)
print(penguin4 * kol)
print(penguin5 * kol)
