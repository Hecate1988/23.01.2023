#Простой калькулятор

while True:
    number1 = float(input("Введите первое число:"))
    number2 = float(input("Введите второе число:"))
    action = (input("Введите действие:+,-,*,/, %, **, //"))
    if action == "+":
        print(number1 + number2)
    elif action == "-":
        print(number1 - number2)
    elif action == "*":
        print(number1 * number2)
    elif action == "/":
        if number2 == 0:
            print("Деление на 0")
        else:
            print(number1 / number2)
    elif action == "%":
        if number2 == 0:
            print("Деление на 0")
        else:
            print(number1 % number2)
    elif action == "//":
        if number2 == 0:
            print("Деление на 0")
        else:
            print(number1 // number2)
    elif action == "**":
        print(number1 ** number2)

    s = input("Будем считать дальше: yes: ?")
    if s == "yes":
      print("Тогда будем считать дальше.")
    else:
            break

