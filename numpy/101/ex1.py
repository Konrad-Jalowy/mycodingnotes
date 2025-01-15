import numpy as np

# 1. Stwórz tablicę 2D
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Tablica 2D:\n", array_2d)

# 2. Suma wszystkich elementów
suma = np.sum(array_2d)
print("Suma wszystkich elementów:", suma)

# 3. Wyodrębnij drugi wiersz
drugi_wiersz = array_2d[1, :]
print("Drugi wiersz:", drugi_wiersz)

# 4. Pomnóż całą tablicę przez 5
tablica_razy_5 = array_2d * 5
print("Tablica pomnożona przez 5:\n", tablica_razy_5)