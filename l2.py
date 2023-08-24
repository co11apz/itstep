def age2(defage):
    if defage < 18:
        print('Не берем')
    elif defage in range(17, 28):
        print('Берем')
    else:
        print('Не берем')
try:
    age = int(input('Введите возраст: '))
    age2(age)
except ValueError:
    print('Вы ввели не возраст')