#Selection Sorting
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

waktu_atlet = [12.5, 11.3, 14.2, 10.8, 13.0]
selection_sort(waktu_atlet)
print("Hasil Sorting Waktu Atlet:", waktu_atlet)

#Insertion Sorting
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

kartu = [5, 2, 8, 3, 1]
insertion_sort(kartu)
print("Kartu setelah sorting:", kartu)

#Merge Sort
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

harga_produk = [50000, 150000, 30000, 120000, 70000]
merge_sort(harga_produk)
print("Harga produk setelah sorting:", harga_produk)

#Quick Sort
def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

harga_produk = [20000, 5000, 15000, 30000, 10000]
hasil_sorting = quick_sort(harga_produk)
print("Harga produk setelah diurutkan:", hasil_sorting)
