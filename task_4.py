"""
Задание 4
"""

def execute_4(arr1, arr2, operation):
    """Алгоритм задания 4"""
    try:
        # Преобразование в число
        def to_number(arr):
            if not arr:
                return 0
            return int(''.join(map(str, arr)))
        
        num1 = to_number(arr1)
        num2 = to_number(arr2)
        
        # Выполнение операции
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        else:
            raise ValueError("Неизвестная операция")
        
        # Преобразование результата
        if result < 0:
            return ['-'] + [int(d) for d in str(abs(result))]
        else:
            return [int(d) for d in str(result)]
    
    except Exception as e:
        raise Exception(f"Ошибка вычислений: {e}")


class Task4Cache:
    """Кэш для задания 4"""
    def __init__(self):
        self.cache = {}
    
    def execute_cached(self, arr1, arr2, operation):
        key = (tuple(arr1), tuple(arr2), operation)
        if key not in self.cache:
            self.cache[key] = execute_4(arr1, arr2, operation)
        return self.cache[key]