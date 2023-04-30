import random
print("Добро пожаловать в игру 'Угадай число'! ")
print("Неизвестный:Внимание!У вас всего пять попыток угадать число!")
print("Неизвестный:Особое внимание! Вводить можно любое максимальное и минимальное число!")
while True:
    min_num = input("Введите минимальное число (или 'выход' для выхода из игры): ")
    if min_num == 'выход':
        print("Вы вышли из игры.")
        print("Неизвестный:Испугался?Ха-ха-ха!")
        exit()
    elif not min_num.isnumeric(): 
        print("Пожалуйста, введите целое число.") 
    else:
        min_num = int(min_num) 
        print("Вы ввели число:", min_num)
        break   
count = 5
while True:
    max_num = input("Введите максимальное число (или 'выход' для выхода из игры): ")
    if max_num == 'выход':
        print("Вы вышли из игры.")
        print("Неизвестный:Испугался?Ха-ха-ха!")
        exit()
    elif not max_num.isnumeric():
        print("Пожалуйста, введите целое число.")
    else:
        max_num = int(max_num)
        if max_num < min_num:
            print("Ошибка: максимальное число меньше минимального!")
        else:
            print("Вы ввели число:", max_num)
            break
    count -= 1
    if count == 0:
        print("У вас закончились попытки. Игра окончена.")
        exit()
    else:
        print("Осталось попыток:", count)
if max_num>=2:  
        print(f"Я загадал число от {min_num} до {max_num}.Попробуйте угадать его за минимальное количество попыток.")
        print("Неизвестный:Я обманул.У вас всего две попытки угадать число.Желаю вам удачи!Ха-ха-ха!!!")
num = random.randint(min_num, max_num)
max_attempt = 2
attempt = 0
count = 0
while max_num < 2:
    print("Максимальное число не может быть меньше 2. Пожалуйста, введите другое значение.")
    print("Неизвестный:Тебе сегодня не везет,не правда ли?Неудачник!Ха-ха-ха!")
    max_num = int(input("Введите верное число: "))
    count += 1
    if count == 2:
        print("Вы ввели неверное число 2 раза. Программа завершается.")
        print("Неизвестный:Прощай,неудачник!")
        exit()
count = 0
while True:
    guess = input("Введите число (или 'выход' для выхода из игры): ")
    if guess == 'выход':
        print(f"Загаданное число было {num}.")
        print("Вы вышли из игры.")
        print("Неизвестный:Трусишка!")
        break   
    if not guess.isdigit() or int(guess) < min_num or int(guess) > max_num:
        print(f"Пожалуйста, введите целое число в диапазоне от {min_num} до {max_num}.")
        count += 1
        if count == 3:
            print("Вы ввели неверное число 3 раза. Программа завершается.")
            print("Неизвестный:Я отпускаю тебя!")
            exit()
        else:
            print(f"У вас осталось {3 - count} попытки ввести правильное число")
        continue    
    guess = int(guess)
    attempt += 1 
    if guess < num:
        print("Загаданное число больше.")
    elif guess > num:
        print("Загаданное число меньше.")
    else:
        print(f"Поздравляю! Вы угадали число за {attempt} попытки.")
        print("Неизвестный:Этого не может быть!")
        print("Конец игры")
        break
    if attempt == max_attempt:
        print(f"К сожалению, вы не угадали число за {max_attempt} попытки.")
        print("Неизвестный:Так тебе и надо!")
        print("Конец игры")
        play_again = input("Хотите продолжить угадывать? (да/нет): ")
        if play_again.lower() != "да":
                print("Конец игры")
                break
        
