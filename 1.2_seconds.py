time = int(input('Введите количество секунд: '))

hours = time // 3600
minutes = (time - (hours * 3600)) // 60
seconds = time - (hours * 3600) - (minutes * 60)

print (f'В формате чч:мм:сс ---> {hours:02}:{minutes:02}:{seconds:02}')
