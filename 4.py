#for in
#ввести 20 чисел, при каждом вводе сила сравнивать его с пердыдущим и если
# оно больше предыдущего выводить слово "БОЛЬШЕ"
# или если меньше выводить слово "МЕНЬШЕ", первое значение задать равным 5
d = 0
a = 20
b = 5 #предыдущее
for i in range(a):
    d = input("Введите число ") #текущее
    if b > int(d):
        print("Меньше")
    else:
        print("Больше")
    b = int(d)
