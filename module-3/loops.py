def list_comprehension():
    numbers = [1,2,3,4,5,6]
    result = []
    
    for num in numbers:
        result.append(num + 1)
    
    return result

print(list_comprehension())