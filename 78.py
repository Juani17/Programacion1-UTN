#Ejercicio 7

def ord(lis):
    integers = [x for x in lis if isinstance(x, int)]
    strings = [x for x in lis if isinstance(x, str)]

    integers.sort()
    strings.sort()

    lis[:] = integers + strings

lis = [9, "Jamon", 25, "Patroclo", 6, "Ajujeño", 46]
ord(lis)
print(lis)



#Ejercicio 8
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
