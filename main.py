import math

def is_valid_triangle(a, b, c):
    return a > 0 and b > 0 and c > 0 and (a + b > c) and (a + c > b) and (b + c > a)

def calculate_area(a, b, c):
    s = (a + b + c) / 2  # полупериметр
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

def task1():
    try:
        a = float(input("Введите длину первой стороны: "))
        b = float(input("Введите длину второй стороны: "))
        c = float(input("Введите длину третьей стороны: "))
        
        if not is_valid_triangle(a, b, c):
            print("Ошибка: Треугольник с такими сторонами не существует.")
            return
        
        if a == b == c:
            print("Треугольник равносторонний.")
        elif a == b or b == c or a == c:
            print("Треугольник равнобедренный.")
        else:
            print("Треугольник разносторонний.")
        
        area = calculate_area(a, b, c)
        print(f"Площадь треугольника: {area:.2f}")
    
    except ValueError:
        print("Ошибка: Введены некорректные данные.")
        
def task3():
    try:
        a = float(input("Введите длину первой стороны: "))
        b = float(input("Введите длину второй стороны: "))
        c = float(input("Введите длину третьей стороны: "))
        
        if not is_valid_triangle(a, b, c):
            print("Ошибка: Треугольник с такими сторонами не существует.")
            return
        
        sides = [a, b, c]
        sides.sort()
        
        if math.isclose(sides[0]**2 + sides[1]**2, sides[2]**2):
            print("Треугольник прямоугольный.")
        elif sides[0]**2 + sides[1]**2 > sides[2]**2:
            print("Треугольник остроугольный.")
        else:
            print("Треугольник тупоугольный.")
    
    except ValueError:
        print("Ошибка: Введены некорректные данные.")

def main():
    while True:
        print("\nВыберите задание:")
        print("1 - Задание: Определить вид треугольника и его площадь")
        print("3 - Задание: Определить тип углов треугольника")
        print("0 - Выход")
        
        choice = input("Ваш выбор: ")
        
        if choice == "1":
            task1()
        elif choice == "3":
            task3()
        elif choice == "0":
            break
        else:
            print("Некорректный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
