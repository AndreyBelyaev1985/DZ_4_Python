

'''

Дан список чисел.
Создать список в который попадают числа, описывающие возрастающую последовательность и содержащие максимальное количество элементов.
Пример: [1,5,2,3,4,6,1,7] => [1,2,3,4,6,7]
[5,2,3,4,,6,1,7] => [2,3,4,6,7]
Порядок менять нельзя

'''

from random import randint
N = [1, 5, 2, 3, 4, 6, 1, 7]


def get_up2(nums):
    ups = []
    minNumber = min(nums)
    for i in nums:
        if i == minNumber:
            ups.append(i)
            minNumber += 1
        elif i == minNumber + 1:
            ups.append(i)
            minNumber += 2
    return ups


print(get_up2(N))

# Создать и заполнить файл случайными целыми значеничми. Выполнить сортировку содержимого файла по возрастанию.


def main(n):
    with open('RandomNum.txt', 'w+') as ran:
        for _ in range(n):
            ran.write(f'{str(randint(1,100))}\n')


N = int(input('Сколько случайных чисел будет храниться в файле? \n'))
main(N)

with open('RandomNum.txt', 'r') as fr:
    List_int = fr.readlines()
    List_int.sort(key=(int))

with open('Sortfile.txt', 'w+') as data:
    for element in List_int:
        data.write(element)
