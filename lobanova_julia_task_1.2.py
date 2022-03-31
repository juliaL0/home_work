some_list = []
new_list = []
final_list = []


def sum_el(n):
    el_sum = 0
    while n > 0:
        digit = n % 10
        n = n // 10
        el_sum += digit
    return el_sum


for i in range(1, 1001):
    if i % 2 != 0:
        i = i ** 3
        some_list.append(i)


for i in some_list:
    if sum_el(i) % 7 == 0:
        new_list.append(i)


for i in some_list:
    i = i + 17
    if sum_el(i) % 7 == 0:
        final_list.append(i)

print(some_list)
print(sum(new_list))
print(sum(final_list))
