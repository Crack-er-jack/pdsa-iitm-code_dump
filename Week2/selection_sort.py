# Implementing Selection Sort

def selection_sort(L):
    n = len(L)
    for i in range(n):
        min_pos = i
        for j in range(i + 1, n):
            if L[j] < L[min_pos]:
                min_pos = j
        L[min_pos], L[i] = L[i], L[min_pos]
    return L

L = [1, 4, 7, 3, 10, 9]
print(selection_sort(L))
