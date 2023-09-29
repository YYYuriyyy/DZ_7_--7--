                          ## Завдання 1
##           Напишіть функцію, яка відобразить на екрані такий форматований текст:
##   "Don't compare yourself with anyone in this world…
##    if you do so, you are insulting yourself."
##    Bill Gates
#
def text():
    print(""" "Don't compare yourself with anyone in this world.
 If you do so, you are insulting yourself."
 Bill Gates""")
text()

                              ## Завдання 2
 ##        Напишіть функцію, яка приймає два числа як параметр і відображає всі парні числа між ними.
#
def display_even_numbers(start, end):
    for num in range(start + 1, end):
        if num % 2 == 0:
            print(num)

display_even_numbers(10, 20)

                            ## Завдання 3
##   Напишіть функцію, яка відображає порожній або заповнений квадрат з певного символу.
##   Функція приймає як параметри довжину сторони квадрата, символ і змінну логічного типу:
##   якщо вона дорівнює True, квадрат заповнений;
##   якщо — False, квадрат порожній.

def draw_square(side_length, symbol, filled):
    if filled:
        for i in range(side_length):
            for j in range(side_length):
                print(symbol, end=' ')
            print()
    else:
        for i in range(side_length):
            for j in range(side_length):
                if i == 0 or i == side_length-1 or j == 0 or j == side_length-1:
                    print(symbol, end=' ')
                else:
                    print(' ', end=' ')
            print()

draw_square(4, "#", True)

draw_square(4, "*", False)

                             ## Завдання 4
## Напишіть функцію, яка повертає мінімальне з п'яти чисел. Числа передаються як параметри

def find_minimum(a, b, c, d, e):
    minimum = a
    if b < minimum:
        minimum = b
    if c < minimum:
        minimum = c
    if d < minimum:
        minimum = d
    if e < minimum:
        minimum = e
    return minimum

result = find_minimum(7, 27, 8, 35, 9)
print(result)

                                   ## Завдання 5

## Напишіть функцію, яка повертає добуток чисел у вказаному діапазоні.
## Межі діапазону передаються як параметри. Якщо межі діапазону переплутані
## (наприклад, 5 — верхня межа, 25 — нижня межа), їх треба поміняти місцям

def multiply_range(lower, upper):
    if lower > upper:
        lower, upper = upper, lower

    result = 1
    for i in range(lower, upper + 1):
        result *= i

    return result

result = multiply_range(5, 25)
print(result)

                                ## Завдання 6
## Напишіть функцію, яка рахує кількість цифр у числі.
## Число передається як параметр. З функції потрібно повернути отриману кількість цифр.
## Наприклад, якщо передали 3456, кількість цифр буде 4.

def count_digits(number):
    return len(str(number))

number = 1234567890987654321
digit_count = count_digits(number)
print(digit_count)

                               ## Завдання 7
## Напишіть функцію, яка перевіряє, чи є число паліндромом. Число передається як параметр.
## Якщо число є паліндромом, потрібно повернути з функції true, якщо ні — false.


def is_palindrome(number):
    number_str = str(number)
    if number_str == number_str[::-1]:
        return True
    else:
        return False

print(is_palindrome(12345678900000987654321))

print(is_palindrome(567))

