########################################################################################################################
i = int(input("процентная ставка в год: ")) # годовая процентная ставка
i = i / 100
n = int(input("кол-во месяцев: ")) # кол-во месяцев
S = int(input("сумма кредита: ")) # сумма кредита
add = 0
# i = 10/1200
# n = 120
# S = 880000
# K = (i * (1+i)**n) / (((1+i)**n) - 1)
# A = S * K
# Decrease = 22500
# print("Сумма кредита: ", S)
# print("Процентная ставка: ", i)
# print("Срок кредита(мес): ", n)
# print("Коэффициент аннуитета: ", K)
# print("Всего в уплату по кредиту: ", A*n)
# print("Ежемесячный платёж: ", A)
# print("Желаемый ежемесячный платёж: ", Decrease)
# print("######################################################")
#
# while S > 0:
#     K = (i * (1 + i) ** n) / (((1 + i) ** n) - 1)       # коэфициент(зависит от n)
#     A = S * K                                           # ежемесячный платёж(учитывается коэфициент)
#     percent = S*i                                       # проценты за пользование кредитными средствами
#     percent = round(percent, 2)
#     # add = Decrease - A
#     # add = round(add, 2)
#     debt = A - percent + add                            # что идёт в погашение долга
#     debt = round(debt, 2)
#     S = S - debt                                        # новое "тело" кредита
#     S = round(S, 2)
#     print("Необходимая добавочная сумма: ", add)
#     print("Сумма платежа:", percent + debt)
#     print("В погашение процентов: ", percent)
#     print("В погашение долга: ", debt)
#     print("В погашение долга(без доп.платежа): ", debt - add)
#     print("Остаток долга: ", S)
#     print(n)
#     n -= 1
# print("Выплата кредита раньше на", n, "мес.")
# print("Управился за", 105 - n, "мес.")
# print("Или за", (105 - n)/12, "лет.")
########################################################################################################################
########################################################################################################################

def fib(x):
    if x == 0 or x == 1:
        return 1
    else:
        return  fib(x - 1) + fib(x - 2)

y = fib(5)
print(y)



########################################################################################################################
# Задача на нахождение множества C(n,k) =
# n, k = map(int, input().split())
# def bunch(n, k):
#     if k > n:
#         return 0
#     elif k == 0:
#         return 1
#     else:
#         return bunch(n - 1, k) + bunch(n - 1, k - 1)
# print(bunch(n, k))
########################################################################################################################
# Задача с нахождением повторяющихся в списке элементов и однократном их выводе на экран
# a = [int(i)for i in input().split()]          # Чтение из строки информации, разбивается по пробелу
# a = [1, 2, 4, 3, 1, 0, 9, 99, 78, 456, 0, 4]
# print('a = ', a)
# for i in range(len(a)):
#     print(i, a[i])
#     if a.count(i) > 1:
#         print('Повторное число: ', i)
########################################################################################################################
# Формирование запроса по ссылке + извлечение данных с оной
# adress = 'https://stepic.org/media/attachments/course67/3.6.3/'
# count = 0                                     # Отдадочная инфрормация
# with open('dataset_3378_3 (2).txt') as r:     # Открываем файйл под именем R
#     url = r.readline().strip()                # Считываем одну строчку, обрезая лишнее
#     get = requests.get(url).text              # Получаем данные со страницы
#
# while get[0] != 'W':
#     get = requests.get(adress+get).text       # Формируем в цикле новый адрес
#     count += 1                                # Отдадочная инфрормация
#     print(count)                              # Отдадочная инфрормация
# print(get)
########################################################################################################################
