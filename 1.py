from math import cos, sin, tan, radians

def get_angle():
    while True:
        try:
            angle = int(input('Введите значение угла в градусах: '))
            return angle
        except ValueError:
            print("Некорректный ввод. Пожалуйста, введите целое число.")

def calculate_trigonometric_functions(angle):
    angle_rad = radians(angle)
    cos_angle = round(cos(angle_rad), 5)
    sin_angle = round(sin(angle_rad), 5)
    tg_angle = round(tan(angle_rad), 5) if cos_angle != 0 else None
    return sin_angle, cos_angle, tg_angle

def print_results(sin_angle, cos_angle, tg_angle):
    print(f'sin(angle) = {sin_angle}')
    print(f'cos(angle) = {cos_angle}')
    if tg_angle is None:
        print('Тангенса не существует (cos(angle) = 0)\n')
    else:
        print(f'tg(angle) = {tg_angle}')

def main():
    angle = get_angle()
    sin_angle, cos_angle, tg_angle = calculate_trigonometric_functions(angle)
    print_results(sin_angle, cos_angle, tg_angle)

if __name__ == "__main__":
    main()
