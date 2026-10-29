import random
import time

# 1. Insertion Sort للقطع الصغيرة
def insertion_sort(arr, left, right):
    for i in range(left + 1, right + 1):
        key = arr[i]
        j = i - 1
        while j >= left and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# دمج نصفي المصفوفة
def merge(arr, left, mid, right):
    left_part = arr[left:mid + 1]
    right_part = arr[mid + 1:right + 1]

    i = j = 0
    k = left

    while i < len(left_part) and j < len(right_part):
        if left_part[i] <= right_part[j]:
            arr[k] = left_part[i]
            i += 1
        else:
            arr[k] = right_part[j]
            j += 1
        k += 1

    while i < len(left_part):
        arr[k] = left_part[i]
        i += 1
        k += 1

    while j < len(right_part):
        arr[k] = right_part[j]
        j += 1
        k += 1

# 2. Hybrid Sort: التحويل لـ Insertion Sort لو الحجم <= k
def hybrid_sort(arr, left, right, k):
    if right - left + 1 <= k:
        insertion_sort(arr, left, right)
    elif left < right:
        mid = (left + right) // 2
        hybrid_sort(arr, left, mid, k)
        hybrid_sort(arr, mid + 1, right, k)
        merge(arr, left, mid, right)

# دالة مساعدة لتشغيل الفرز
def sort_with_cutoff(data, k):
    arr_copy = data.copy()
    hybrid_sort(arr_copy, 0, len(arr_copy) - 1, k)
    return arr_copy

if __name__ == "__main__":
    DATA_SIZE = 10000
    print(f"Generating random dataset with {DATA_SIZE} elements...")
    dataset = [random.randint(1, 100000) for _ in range(DATA_SIZE)]

    # تجربة قيم مختلفة لقيمة k (Cutoff)
    k_values = [1, 5, 10, 15, 20, 30, 50, 100]
    
    print("\n-------------------------------------------")
    print(f"{'Cutoff (k)':<15} | {'Execution Time (Seconds)':<25}")
    print("-------------------------------------------")

    best_k = None
    min_time = float("inf")

    for k in k_values:
        start_time = time.perf_counter()
        sort_with_cutoff(dataset, k)
        elapsed_time = time.perf_counter() - start_time

        print(f"k = {k:<11} | {elapsed_time:.6f} s")

        if elapsed_time < min_time:
            min_time = elapsed_time
            best_k = k

    print("-------------------------------------------")
    print(f"[✔] Best Cutoff Value: k = {best_k} (Time: {min_time:.6f} s)")