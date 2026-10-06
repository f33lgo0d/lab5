n = int(input("Ввведи мне число количество чисел N: "))

numbers = [] 
print("Введи мне числа через пробел иди с новой строки")

for i in range(n):
    num = int(input(f"Число {i+1}:"))
    numbers.append(num)

sum_even = 0
count_even = 0
sum_odd = 0
count_odd = 0

for num in numbers:
    if num % 2 == 0:

        sum_even += num
        count_even += 1
    else:
        sum_odd += num
        count_odd += 1
        
if count_even > 0:
    avg_even = sum_even / count_even
else:
    avg_even = 0

if count_odd > 0:
    avg_odd = sum_odd / count_odd
else:
    avg_odd = 0

result = avg_even - avg_odd

print(f"Среднее арифметическое четных: {avg_even}")
print(f"Среднее арифметическое нечетных: {avg_odd}")
print(f"Разность (четные - нечетные): {result}")
