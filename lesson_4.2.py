x = int(input())
s_s = 0 #
s_p = 0 #
line = 0
while x > 0:
    line += 1 # число чисел
    s_s += x # сумма чисел
    s_p *= x # произведение чисел
    aver = s_s / line # среднее арефметическое
    x = int(input())
print(line)
print(s_s)
print(s_p)
print(aver)
    

