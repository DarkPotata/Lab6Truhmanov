# Простой калькулятор
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Ошибка: деление на ноль"
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    return a % b

# Главная функция
def main():
    x = 10
    y = 5
    print(f"Сложение: {add(x, y)}")
    print(f"Вычитание: {subtract(x, y)}")
    print(f"Умножение: {multiply(x, y)}")
    print(f"Деление: {divide(x, y)}")
    print(f"Степень: {power(x, y)}")
    print(f"Остаток: {modulo(x, y)}")

if __name__ == "__main__":
    main()
