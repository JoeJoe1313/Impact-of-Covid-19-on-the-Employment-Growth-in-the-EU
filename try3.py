def merge_sort(l):
    if len(l) > 1:
        # find the middle and split the array into two halves
        mid = len(l) // 2
        left = l[:mid]
        right = l[mid:]

        # call merge_sort() for the left half
        merge_sort(left)

        # call merge_sort for the right half
        merge_sort(right)

        # merge the two halves from the above two calls
        # i - iterate over left half, j - iterate over right half
        i = j = 0
        # iterate over the main list - l
        k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                l[k] = left[i]
                i += 1
            else:
                l[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            l[k] = right[j]
            j += 1
            k += 1
    return l


l = [14, 46, 43, 27, 57, 41, 45, 21]
print(merge_sort(l))
