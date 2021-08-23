#2. Написать два алгоритма нахождения i-го по счёту простого числа.
#Без использования «Решета Эратосфена»;
#Используя алгоритм «Решето Эратосфена»
#Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.
import cProfile

def sieve_eratosthenes(n):
    numbers = list(range(2, n + 1))
    for number in numbers:
        if number != 0:
            for candidate in range(2 * number, n+1, number):
                numbers[candidate-2] = 0
    print (*list(filter(lambda x: x != 0, numbers)))




def without_sieve_eratosthenes(n):
    numbers=[]

    for i in range (2,n+1):
        flag = True
        for j in range(i-1 , 1 , -1):
            if i%j==0:
                flag = False
                break
        if flag == True:
            numbers.append(i)

    print(numbers)


def main():
    without_sieve_eratosthenes(10000)
    sieve_eratosthenes(10000)



if __name__ == '__main__':
    cProfile.run('main()')






#Функция не использующая алгоритм 'Решето Эратосфена' выполняется в 100 раз дольше, чем фунция использующая данный алгоритм