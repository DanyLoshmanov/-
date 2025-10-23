def sum_all(*args):
    total = 0
    for numbers in args:
        total += numbers
    return total
    
result = sum_all(1,3,5,10)
result_2 = sum_all()

print(result)
print(result_2)