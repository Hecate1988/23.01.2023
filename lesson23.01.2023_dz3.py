n = int(input("Введите любое 5-тизначное целое положительное число: "))
print(n % 10 * 10000 + n // 10 % 10 * 1000 + n // 100 % 10 * 100 + n // 1000 % 10 * 10 + n // 10000 % 10)