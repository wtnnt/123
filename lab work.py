#1
a = 14 #int
b = 4.52 #float
c = "сторка" #str
d = True #bool

#2
a = "Кирилл"
b = 18
print(f'Задание №2: {a} {b}')

#3
a = 342
b = 56.2
c = "43"
x = a+b+int(c)
print(f'Задание №3: {x}')

#4
a = 8
b = 3
x = ((a+4*b)*(a-3*b)+(a**2))
print(f'Задание №4: {x}')

#5
a = int(input())
b = int(input())
S = a*b
P = 2*(a+b)
print(f"Задание №5: Площадь равна {S} Периметр равен {P}")

#6
first = "*   *   *"
second = " * * * * "
third = "  *   *  "
print('Задание №6:')
print(first)
print(second)
print(third)

#7
a = 69
b = 52
print('Задание №7:')
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")
print(f"{a} < {b} = {a < b}")
print(f"{a} > {b} = {a > b}")
print(f"{a} <= {b} = {a <= b}")
print(f"{a} >= {b} = {a >= b}")
print(f"{a} != {b} = {a != b}")

#8
name = "Кирилл"
age = 18
print(f'Задание №8: Меня зовут {name}, мне {age} лет')

#9
sentence = 'Съешь ещё этих мягких французских булок, да выпей чаю'
print("Задание №9:")
words = sentence.split()
for word in words:
    print(word)
reconstructed_sentence = ""
for i in range(len(words)):
    if i == len(words) - 1:
        reconstructed_sentence += words[i]
    else:
        reconstructed_sentence += words[i] + " "

print(reconstructed_sentence)



#10
a = "нет!да!"
print(f'Задание №10: {a*4}')

#11
a = input('Введите три числа через запятую: ')
b = list(map(int, a.split(',')))
first = b[0]
second = b[1]
third = b[2]
x = ((first + third) // second)
print(f'Задание №11: Результат вычисления: {x}')

#12
a = "компьютеры"
print("Задание №12:")
print(a[:4])
print(a[8:])
print(a[3:8:])
print(a[::-1])