def sum_iterative(n):
    total = 0
    for i in range(1, n+1):
        total += i
        return total

def sum_formula(n):
    return n * (n + 1) // 2
print(sum_iterative(10))
print(sum_formula(10))