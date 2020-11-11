# Даны два целых числа `A` и `В`.
# Выведите все числа от `A` до `B` включительно, в порядке возрастания, если `A < B`,
# или в порядке убывания в противном случае.
# Вариант №1
a = int(input('enter some number "A" - '))
b = int(input('enter some number "B" - '))
if a < b:
    for i in range(a, b + 1, 1):
        print(i, end=' ')
else:
    for e in reversed(range(b, a + 1, 1)):
        print(e, end=' ')
print('\n') #для удобства запуска всех программ в разделе
# Вариант №2
a = int(input('enter some number "A" - '))
b = int(input('enter some number "B" - '))
if a < b:
    for i in range(a, b + 1, 1):
        print(i, end=' ')
else:
    temp = a
    a = b
    b = temp
    for e in reversed(range(a, b + 1, 1)):
        print(e, end=' ')

print('\n')
#Вариант №3
a = int(input('enter some number "A" - '))
b = int(input('enter some number "B" - '))
def fun_list1(a, b):
    for i in range(a, b + 1, 1):
        print(i, end=' ')
def fun_list2(a, b):
    for e in reversed(range(b, a + 1, 1)):
        print(e, end=' ')
if a < b:
    print(fun_list1(a, b)) #не могу понять, почему в конце списка выдает - "None"
else:
    print(fun_list2(a, b)) #не разобрался как развернуть функцию