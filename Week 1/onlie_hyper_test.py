li = []
n = int(input())
for i in range(n):
    li.append(int(input()))

def kadane_algorithm(A):
    max_global = max_current = 0
    for i in range(0, len(A)):
        max_current = max(A[i], max_current + A[i])
        max_global = max(max_global, max_current)
    return max_global

result = kadane_algorithm(li)
print(result)