def delenie(x):
    y = 100 / x
    return y
try:
    x = int(input('введите число: '))
except ValueError:
    print('ошибка! введено не число')
except ZeroDivisionError:
    print('ошибка! на 0 делить нельзя')
result = delenie(x)

print(result)
