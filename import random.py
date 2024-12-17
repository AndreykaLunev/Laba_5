import random

def print_intro():
    print("Добро пожаловать в игру 'Камни'!")
    print("В этой игре вы будете играть против компьютера.")
    print("Вы можете взять 1, 2 или 3 камня за ход.")
    print("Тот, кто оставляет последнего камня сопернику, выигрывает.")
    print()

def get_user_move(remaining_stones):
    while True:
        try:
            move = int(input(f"Сколько камней вы хотите взять? (1, 2 или 3): "))
            if move in [1, 2, 3] and move <= remaining_stones:
                return move
            else:
                print(f"Пожалуйста, введите число от 1 до 3, не превышающее количество оставшихся камней ({remaining_stones}).")
        except ValueError:
            print("Пожалуйста, введите корректное число.")

def get_computer_move(remaining_stones):
    return random.randint(1, min(3, remaining_stones))

def main():
    print_intro()
    
    remaining_stones = random.randint(4, 30)
    print(f"В начале игры у нас {remaining_stones} камней.")

    while remaining_stones > 0:
        user_move = get_user_move(remaining_stones)
        remaining_stones -= user_move
        print(f"Вы взяли {user_move} камней. Осталось {remaining_stones} камней.")

        if remaining_stones == 0:
            print("Вы оставили последнего камня сопернику. Вы проиграли!")
            break

     
        computer_move = get_computer_move(remaining_stones)
        remaining_stones -= computer_move
        print(f"Компьютер взял {computer_move} камней. Осталось {remaining_stones} камней.")

        if remaining_stones == 0:
            print("Компьютер оставил последнего камня вам. Вы выиграли!")
            break

main()