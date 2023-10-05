size = 6
for i in range(size // 2, size, 2):
    print(' ' * (size - i) + '* ' * i)
for i in range(size, 0, -1):
    print(' ' * (size - i) + '* ' * i)