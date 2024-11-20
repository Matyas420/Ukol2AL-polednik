import random

# Vytvoření jednorozměrného pole s 10 náhodnými hodnotami
array1 = [random.randint(0, 100) for _ in range(10)]

# Seřazení pole
serazeni = sorted(array1)

print(array1)
print(serazeni)
