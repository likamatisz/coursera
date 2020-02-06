num = int(input())
firstNum = num // 10 // 10 % 10
secondNum = num // 10 % 10
thirdNum = num % 10
print(firstNum + secondNum + thirdNum)