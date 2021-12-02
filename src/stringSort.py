arr=['banana', 'apple', 'pear', 'pineapple', 'peach']
print(*sorted(arr, key=len))
print(*sorted(arr, key=lambda x:(x[2], len(x))))