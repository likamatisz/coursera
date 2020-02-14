# Даны три целых числа. Найдите наибольшее из них (программа должна вывести ровно одно целое число).
first = int(input())
second = int(input())
third = int(input())
if second <= first >= third:
    print(first)
elif first <= second >= third:
    print(second)
else:
    print(third)
