"""
5. Напишите свою собственную игру - камень ножницы бумага
Игра должна идти до 3-х побед, и выводить кто победил . Играют комп и человек
Для реализации игры "Камень, ножницы, бумага" между компьютером и человеком до трех побед можно использовать Python. Программа будет случайным образом выбирать действия компьютера и учитывать ввод пользователя. Также будет вестись подсчет очков, и игра завершится, когда кто-то наберет 3 победы. Вот пример такой программы:
"""

import random

def get_computer_choice():
    return random.choice(["камень", "ножницы", "бумага"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Ничья"
    elif (user_choice == "камень" and computer_choice == "ножницы") or \
         (user_choice == "ножницы" and computer_choice == "бумага") or \
         (user_choice == "бумага" and computer_choice == "камень"):
        return "Человек"
    else:
        return "Компьютер"

def main():
    user_wins = 0
    computer_wins = 0
    winning_score = 3

    while user_wins < winning_score and computer_wins < winning_score:
        user_choice = input("Выберите камень, ножницы или бумага: ").lower()

        if user_choice not in ["камень", "ножницы", "бумага"]:
            print("Неправильный ввод. Пожалуйста, выберите камень, ножницы или бумага.")
            continue

        computer_choice = get_computer_choice()
        print(f"Компьютер выбрал: {computer_choice}")

        winner = determine_winner(user_choice, computer_choice)
        if winner == "Человек":
            user_wins += 1
            print("Вы выиграли этот раунд!")
        elif winner == "Компьютер":
            computer_wins += 1
            print("Компьютер выиграл этот раунд!")
        else:
            print("Этот раунд ничья.")

        print(f"Счет: Человек {user_wins} - {computer_wins} Компьютер\n")

    if user_wins == winning_score:
        print("Поздравляем! Вы выиграли игру!")
    else:
        print("Компьютер выиграл игру. Удачи в следующий раз!")

if __name__ == "__main__":
    main()

"""
### Объяснение:
1. **Функция `get_computer_choice`**: Возвращает случайный выбор компьютера из списка возможных вариантов.
2. **Функция `determine_winner`**: Определяет победителя текущего раунда, сравнивая выборы игрока и 
компьютера.
3. **Основная функция `main`**:
   - Ведет подсчет побед для игрока и компьютера.
   - Запрашивает у пользователя его выбор и проверяет, корректен ли он.
   - Сравнивает выборы и обновляет счет.
   - Игра продолжается, пока один из игроков не наберет 3 победы.
4. **Вывод результатов**: После окончания игры выводится сообщение о победителе.
"""