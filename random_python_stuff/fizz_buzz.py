"""My implementation of fizzbuzz."""

import demo_main

def fizzbuzz(number):
        if number % 3 == 0 and number % 5 != 0:
             print('fizz')
        if number % 5 == 0 and number % 3 != 0:
            print('buzz')
        if number % 3== 0 and number % 5== 0:
            print('fizzbuzz')

fizzbuzz(10)

"""

def grocery_list(dairy_name, produce_name, meat_name):
    return '{dairy_name}, {produce_name}, {meat_name}'

grocery_list('milk' , 'apples' , 'steak')
"""

if __name__ == '__main__':
    fizzbuzz(15)
    demo_main.my_funky_function('file transfer')
