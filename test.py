from math import sqrt

message: str = ('Добро пожаловать в самую лучшую программу для'
                ' вычисления квадратного корня из заданного числа')
print(message)


def calculate_square_root(number: float) -> float:
    """Вычисляет квадратный корень."""
    return sqrt(number)


def calc(your_number: float) -> str:
    """Док функции calc."""
    if your_number <= 0:
        return

    calc_sqrt = calculate_square_root(your_number)
    print(f'Мы вычислили квадратный корень из введённого вами числа.'
          f' Это будет: {calc_sqrt}')


print(message)
calc(25.5)