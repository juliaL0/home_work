duration = int(input('Введите количество секунд: '))
if duration < 60:
    print(f'{duration} sec')
elif duration < 3600:
    duration_m = duration // 60
    duration_s = duration % 60
    print(f'{duration_m} min {duration_s} sec')
elif 3600 <= duration < 86400:
    duration_h = duration // 3600
    duration_m = (duration % 3600) // 60
    duration_s = (duration % 3600) % 60
    print(f'{duration_h} h {duration_m} min {duration_s} sec')