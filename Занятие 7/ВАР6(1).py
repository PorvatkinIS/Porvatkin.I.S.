def count_max(s):
    max_elem = max(s)
    mensh_count = sum(1 for elem in s if elem < max_elem)
    bolsh_count = sum(1 for elem in s if elem > max_elem)
    return mensh_count, bolsh_count
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mensh, bolsh = count_max(arr)
print("Количество элементов, меньших максимального:", mensh)
print("Количество элементов, больших максимального:", bolsh)
