import numpy as np
def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    
    # предполагаемое число
    predict = np.random.randint(1, 101)
    # Счетчик попыток
    count = 0    
    
    if number > predict:
        # В цикле сокращаем диапазон поиска до 10 чисел, 
        # увеличивая predict с шагом = 10
        while number > predict:
            count += 1
            predict += 10
        # В найденном десятке находим заданое число, 
        # уменьшая predict с шагом = 1
        while number < predict:
            count += 1
            predict -= 1

    elif number < predict:
        # В цикле сокращаем диапазон поиска до 10 чисел, 
        # уменьшая predict с шагом = 10
        while number < predict:
            count += 1
            predict -= 10
        # В найденном десятке находим заданое число, 
        # увеличивая predict с шагом = 1
        while number > predict:
            count += 1
            predict += 1
        
    # Ваш код заканчивается здесь

    return count
if __name__ == '__main__' :
   print('\nTotal count: ', game_core_v3(18))
