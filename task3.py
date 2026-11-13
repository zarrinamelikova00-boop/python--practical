
number = 37
attempts = 5

while attempts > 0:
    guess = int(input("Угадайте число: "))

    if guess == number:
        print("Угадал!")
        break
    elif guess > number:
        print("Меньше!")
    else:
        print("Больше!")

    attempts = attempts - 1
    print("Осталось попыток:", attempts)

if attempts == 0:
    print("Попытки закончились!")
    print("Правильный ответ:", number)
