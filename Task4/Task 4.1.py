#1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
#Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

import cProfile

def first(i):
    n = int(i)
    even = odd = 0
    while n > 0:
        if n % 2 == 0:
            even += 1
        else:
            odd += 1
        n = n // 10
    print("четных - %d, нечетных - %d" % (even, odd))



def second(i):
    a = i
    even = 0
    odd = 0
    for i in range(len(a)):
        if a[i].isdigit() and int(a[i]) % 2 == 0:
            even += 1
        if a[i].isdigit() and int(a[i]) % 2 == 1:
            odd += 1

    print(f'В числе чётных {even} и {odd} нечётных чисел ')


def main():
    first('1232143515241253112434135251251353123154783792194312434153152531424153157327'*1000)
    second('1232143515241253112434135251251353123154783792194312434153152531424153157327'*1000)



if __name__ == '__main__':
    cProfile.run('main()')

    # Первый алгоритм работает во много раз медленнее второго