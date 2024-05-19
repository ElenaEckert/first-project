def game_core_v4(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    
    # Определяем диапазон поиска от 1 до 100    
    min_num = 1
    max_num = 100
    
    # Делим диапазон пополам предполагаемым числом
    predict = (min_num + max_num) // 2
    
    # Инициализируем счетчик попыток, первая уже была 
    count = 1    
    
    # В каждом проходе цикла сокращаем диапазон поиска вдвое, 
    # пока не будет найдено заданное число
    while number != predict:
        
        count += 1
        if number > predict:           
            
            min_num = predict + 1 
                   
        elif number < predict:
            
            max_num = predict - 1
            
        predict = (min_num + max_num) // 2               

    return count

if __name__ == '__main__' :
    print(f'Число попыток: {game_core_v4(64)}')