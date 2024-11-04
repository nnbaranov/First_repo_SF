import numpy as np

def game_core_v3(number: int=1) -> int:
    """Угадываем число менее, чем за 20 попыток
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Параметры диапозона:
    low = 1 
    hight = 100
    count = 0 
    
    while low <= hight:
        count += 1
        
        # Находим середину диапозона:    
        guess = (low + hight) // 2
        
        if guess == number:
            break
        
        elif guess < number:
            low = guess + 1
            
        else: 
            hight = guess - 1
             
    return count

print(game_core_v3(10))


def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 10000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(10000))  # загадали список чисел

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")

print('Run benchmarking for game_core_v3: ', end='')
score_game(game_core_v3)
    
    