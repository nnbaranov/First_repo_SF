import numpy as np
def random_predict(number: int=1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: попыток 
    """
    count = 0 
    
    while True:
        count += 1 
        predict_number = np.random.randint(1, 100)
        if number == predict_number:
            break
    return count

print(f'Отгадали число за {random_predict()} попыток')

a = 1 + 2
print(a)

        