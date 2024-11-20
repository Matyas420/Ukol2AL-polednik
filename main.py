import random

# Vytvoření jednorozměrného pole s 10 náhodnými hodnotami
random_array = [random.randint(0, 100) for _ in range(10)]

# Jednoduché seřazení pole
sorted_array = sorted(random_array)

print(random_array)
print(sorted_array)
