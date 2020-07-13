def print_pyramid(n):
    if n == 0:
        pass
    else:
        print_pyramid(n-1)
        layer = []
        for x in range(n):
            layer.append('#')
        print(layer)


print_pyramid(4)

print('\n')
print_pyramid(5)

print('\n')
print_pyramid(20)
