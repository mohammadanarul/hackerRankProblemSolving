n = int(input())
arr = list(map(int, input().split()))

max_number = max(arr)
max_number_count = arr.count(max_number)
for i in range(max_number_count):
    arr.remove(max_number)
print(max_number)
