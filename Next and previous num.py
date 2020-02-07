# Напишите программу, которая считывает целое число и выводит текст, аналогичный приведенному в примере (важно в
# точности соблюдать вывод программы: обратите внимание на пробелы и на точки). Нельзя пользоваться конкатенацией
# строк, используйте print с несколькими параметрами.
num = int(input())
nextNum = num + 1
preNum = num - 1
print('The next number for the number ', num, ' is ', nextNum, '.', sep='')
print('The previous number for the number ', num, ' is ', preNum, '.', sep='')
