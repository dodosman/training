nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
celcius = {'t1': 20, 't2': 33, 't4': 40, 't5': -5, 't6': -12}
powered_nums = []
for elem in nums:
    powered_nums.append(elem ** 2)
    # print(powered_nums)
    # print([elem ** 2 for elem in nums])

even_nums = [elem
             for elem in range(94050)
             if elem % 2 == 1]
# print(even_nums)

"""
wyrazenie słownikowe
"""
numbers = [1, 5, 6, 4, 3, 1, 21]

multiplied_nums = {number: number * (number * 2)
                   for number in numbers}
# print(multiplied_nums)

farenheit = {
    key: celcius * 1.8 + 32
    for key,celcius in celcius.items()
    if celcius >= 5
       if celcius <= 30
}
print(farenheit)

#num podzielne przez 7 ale nie podzielne przez 5, range(100,471)

num_devidable = [elem
                 for elem in range(100,471)
                 if elem % 7 == 0
                 if elem %5 != 0
                 ]
print(num_devidable)