from math import cos, sin, tan, radians

try:
    angle = int(input('Введите значение угла в градусах\n'))
except:
    exit ("Incorrect input\n")
angle = radians(angle)
cos_angle = round(cos(angle), 5)
sin_angle = round(sin(angle), 5)
tg_angle = round(tan(angle), 5)

print(f'sin(angle) = {sin_angle}')
print(f'cos(angle) = {cos_angle}')
if cos_angle == 0:
    print('Тангенса не существует\n')
else:
    print(f'tg(angle) = {tg_angle}')
