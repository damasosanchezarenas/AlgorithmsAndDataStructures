def shell_sort(elements):
    size = len(elements)
    gap = size // 2

    while gap > 0:
        for i in range(gap, size):
            anchor = elements[i]
            j = i
            while j>= gap and elements[j-gap] > anchor :
                elements[j] = elements[j-gap]
                j -= gap

            elements[j] = anchor
        gap = gap // 2

if __name__ == '__main__':
    elements = [11,9,29,7,2,15,28]
    shell_sort(elements)
    print(elements)