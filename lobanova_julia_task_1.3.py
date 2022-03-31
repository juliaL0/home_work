for i in range(1, 101):
    if i % 10 == 0:
        print(f'{i} процентов')
    elif i % 10 == 1 and i != 11:
        print(f'{i} процент')
    elif i % 10 == 2 and i != 12:
        print(f'{i} процента')
    elif i % 10 == 3 and i != 13:
        print(f'{i} процента')
    elif i % 10 == 4 and i != 14:
        print(f'{i} процента')
    elif i % 10 == 5:
        print(f'{i} процентов')
    elif i % 10 == 6:
        print(f'{i} процентов')
    elif i % 10 == 7:
        print(f'{i} процентов')
    elif i % 10 == 8:
        print(f'{i} процентов')
    elif i % 10 == 9:
        print(f'{i} процентов')
    elif i == 11 or i == 12 or i == 13 or i == 14:
        print(f'{i} процентов')
