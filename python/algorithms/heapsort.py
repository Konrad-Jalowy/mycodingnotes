def heapify(arr, n, i):
    largest = i  # Inicjuj największy jako korzeń
    left = 2 * i + 1  # Lewy dzieciak
    right = 2 * i + 2  # Prawy dzieciak

    # Sprawdź, czy lewe dziecko jest większe niż korzeń
    if left < n and arr[i] < arr[left]:
        largest = left

    # Sprawdź, czy prawe dziecko jest większe niż korzeń
    if right < n and arr[largest] < arr[right]:
        largest = right

    # Zmiana miejscami, jeśli korzeń nie jest największy
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Zamień

        # Rekurencyjnie heapify na zmienionym poddrzewie
        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)

    # Budowanie kopca (Max-Heap)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Jeden po drugim wyciągaj elementy z kopca
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Zamień
        heapify(arr, i, 0)

# Przykład użycia
arr = [12, 11, 13, 5, 6, 7]
heapSort(arr)
print("Posortowana tablica:", arr)
