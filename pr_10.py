def find_max():
    
    num = int(input())

    
    if num == 0:
        return 0

    
    rest_max = find_max()

    
    return max(num, rest_max)


result = find_max()
print(f"Наибольшее значение в последовательности: {result}")
