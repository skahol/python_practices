def number_generator(n):
    number = 0
    while number < n:
        if number%5 == 0 and number%7 == 0:
            yield number
        number += 1

    yield -1

n = input("Enter number :")
gen = number_generator(int(n))

my_list = []
while True:
    temp = next(gen)
    if temp == -1:
        break
    else: 
        my_list.append(str(temp))

print(",".join(my_list))