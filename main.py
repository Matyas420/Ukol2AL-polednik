import random

# Vytvoření jednorozměrného pole s 10 náhodnými hodnotami
array1 = [11, 54, 87, 65, 3, 24, 97, 14, 37, 60]

def bubble_sort():
    n = len(array1)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array1[j] > array1[j+1] :
                array1[j], array1[j+1] = array1[j+1], array1[j]
            print(array1)
        return array1
print(bubble_sort())          

array3 = [3, 1, 2, 5, 4]
def bogo_sort(bogo):
    return bogo == sorted(bogo)

def bogosort(bogo):
    while not bogo_sort(bogo):
        random.shuffle(bogo)
    return bogo

print("Předtím:", array3)
print("Potom:", bogosort(array3))
