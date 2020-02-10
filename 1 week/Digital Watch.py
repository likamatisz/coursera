# Электронные часы показывают время в формате h:mm:ss, то есть сначала записывается количество часов (число от 0 до
# 23), потом обязательно двузначное количество минут, затем обязательно двузначное количество секунд. Количество
# минут и секунд при необходимости дополняются до двузначного числа нулями.
# С начала суток прошло N секунд. Выведите, что покажут часы.
t = int(input())
h = (t // 3600) % 24
m1 = t // 60 % 60 // 10
m2 = t // 60 % 60 % 10
s1 = t % 60 // 10
s2 = t % 10
print(h, ":", m1, m2, ":", s1, s2, sep="")
