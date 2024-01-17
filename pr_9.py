def reverse_number(n):
    
    if n < 10:
        return n

    
    return int(str(n % 10) + str(reverse_number(n // 10)))


number = 12345
result = reverse_number(number)
print(f"Число {number} в обратном порядке: {result}")
