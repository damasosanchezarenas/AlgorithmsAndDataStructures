def merge_two_sorted_lists(a,b, arr):

    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1

        k += 1

    #When j has finished
    while i < len_a:
        arr[k] = a[i]
        i +=1
        k += 1

    #When i has finished
    while j < len_a:
        arr[k] = b[j]
        j += 1
        k += 1

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    merge_sort(elements)
    print(f'sorted array: {elements}')