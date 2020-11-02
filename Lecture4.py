# List Comprehension
# 1)
# nums = [x for x in range(1,11)]
# nums = []
# for x in range(1,11):         # raznitsa ---> menshe vremeny
#     nums.append(x)
# nums = list(range(1,11))
# nums = [x for x in range(1,11) if x % 2 ==0]
# print(nums)

# 2)
# numbers = [-1, 9, 34, -43, 0, 9]
# nums = [x // 3 if x % 3 == 0 else 0  for x in numbers if x > 0]
# print(nums)

                # DICT Comprehension ---------> 
# some_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# some_dict['f'] = 4
# new_dict = {}

## print(some_dict.items())
# for key, value in some_dict.items():
#     new_dict[value] = key
# print(new_dict)
    ## print(key)
    ## print(value)
# dict_ = {value *2: key if value == 1 else key for key, value in some_dict.items() if value % 2}
# print(dict_)


# SET Comprehension ----->

# some_set = {'aijana', 'atabek', 'Baytik', 'larisa'}
# new_set = {name.capitalize() for name in some_set if name.startswith('a')}
# print(new_set)

# d = {'a': 1, 'b': 2, 'c': 3}
# for x in d.values():
#     print(x)


# d = {'a': 1, 'b': 2, 'c': 3}
# for x,y in d.values():
#     print(x)

#[1,2,3,4,5,6,7,8,9] ---> My hotim poluchit
# list_ = [
#     [1,2,3],
#     [4,5,6],
#     [7,8,9]                                              # On ----> obychnyi sikl, lineynaya vesh      (100000)
# ]                                                        # On^2 -----> vlojnyi sikl, ne effectivnyi       (10000000000)
# new_list = []                                           # O logn ---> opredelitelnsti effecto coda, obratnyi sisteme
# for item in list_ :                                   # O log^2n ----> 
#     for i in item:
#         new_list.append(i)
# print(new_list)
# flag = True
# while flag:
#     num = 8
#     num2 = input('Enter a number: ')
#     try:
#         num2 = int(num2)
#     except ValueError:
#         print('Incorrect informations!!!')
#         continue
#     try:
#         res = num / num2
#         print(res)
#         break
#     except ZeroDivisionError:
#         print('Divide to ZERO prohibited!!!')
#         continue
#     finally:
#         print('HERE IS YOUR FREAKING RESULT')

num1 = int(input('Enter your first number: '))
num2 = int(input('Enter your second number: '))
try:
    res = num1 / num2
    print(res)
except ZeroDivisionError:   
    print('Divide to zero PROHIBITED!!!🤓')
    # raise Exception('Divide to zero PROHIBITED!!!')
else:
    print('No errors:)')
finally:    
    print('WOOOWW!!😂 ')






























