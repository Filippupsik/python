def func(a, b):
    try:
        return a / b
    except:
        print("На ноль делить нельзя")
a = int(input("Введите 1 число: "))
b = int(input("Введите 2 число: "))
print(func(a, b))