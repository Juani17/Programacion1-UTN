#Ejercicio ordenamiento y busqueda

# Lista a utilizar My_list = (54, 7, 12, 3, 75, 9, 4, 18, 17,24, 23, 86)

''' Metodo de Burbuja '''
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

my_list = [54, 7, 12, 3, 75, 9, 4, 18, 17, 24, 23, 86]
bubble_sort(my_list)
print(my_list)

''' Metodo de Selecion '''
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

my_list = [54, 7, 12, 3, 75, 9, 4, 18, 17, 24, 23, 86]
selection_sort(my_list)
print(my_list)

''' Metodo de insercion '''
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

my_list = [54, 7, 12, 3, 75, 9, 4, 18, 17, 24, 23, 86]
insertion_sort(my_list)
print(my_list)

''' Combinar Ordenamito '''
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

my_list = [54, 7, 12, 3, 75, 9, 4, 18, 17, 24, 23, 86]
merge_sort(my_list)
print(my_list)

''' Busqueda Lienal '''
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

my_list = [3, 4, 7, 9, 12, 17, 18, 23, 24, 54, 75, 86]
target = 12

result = linear_search(my_list, target)

if result != -1:
    print(f"La búsqueda lineal encontró el elemento {target} en la posición {result}.")
else:
    print(f"La búsqueda lineal no encontró el elemento {target}.")
    
''' Busqueda Binaria '''
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

my_list = [3, 4, 7, 9, 12, 17, 18, 23, 24, 54, 75, 86]
target = 12

result = binary_search(my_list, target)

if result != -1:
    print(f"La búsqueda binaria encontró el elemento {target} en la posición {result}.")
else:
    print(f"La búsqueda binaria no encontró el elemento {target}.")
