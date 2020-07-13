def get_factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * get_factorial(n-1)


print(get_factorial(5))
print(get_factorial(6))


def get_factorial_iterative(n):
    result = 1
    for i in range(0, n):
        result += i * result
    return result
      

print(get_factorial_iterative(5))
print(get_factorial_iterative(6))