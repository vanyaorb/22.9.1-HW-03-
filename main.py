# Функция для выполнения двоичного поиска
def binary_search(array, element, left, right):
    if left > right:
        return False

    middle = (right + left) // 2

    if array[middle] == element:
        return middle
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)

# Функция для сортировки последовательности
def custom_sort(sequence):
    return sorted(sequence)

# Основная функция
def main():
    try:
        # Запрос у пользователя последовательности чисел и числа для поиска
        sequence = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
        target_number = int(input("Введите любое число: "))
    except ValueError:
        print("Ошибка: Введены некорректные данные")
        return

    # Сортировка последовательности чисел
    sequence = custom_sort(sequence)

    # Переменная для хранения позиции элемента
    position = None

    # Итерируемся по отсортированной последовательности
    for i in range(len(sequence)):
        # Поиск позиции элемента, который меньше введенного числа, а следующий за ним больше или равен этому числу
        if sequence[i] < target_number:
            continue
        elif sequence[i] >= target_number:
            position = i
            break

    # Вывод сообщения об ошибке, если не удалось найти подходящий элемент
    if position is None:
        print("Ошибка: Элемент не соответствует условию")
    else:
        # Вывод найденной позиции
        print(f"Позиция элемента: {position}")

if __name__ == "__main__":
    main()