# Даны два момента времени в пределах одних и тех же суток. Для каждого момента указан час, минута и секунда.
# Известно, что второй момент времени наступил не раньше первого.
# Определите сколько секунд прошло между двумя моментами времени.
a = int(input())
b = int(input())
c = int(input())
x = int(input())
y = int(input())
z = int(input())
print((x - a) * 3600 + (y - b) * 60 + z - c)
