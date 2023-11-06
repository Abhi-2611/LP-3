import time
start = time.time()

val = [int(x) for x in input("Enter item profit : ").split()]
wt = [int(x) for x in input("Enter item weights : ").split()]
W = int(input("Enter the knapsack's weight capacity: "))
n = len(val)
K = [[0 for x in range(W + 1)] for x in range(n + 1)]

for i in range(n + 1):
    for w in range(W + 1):
        if i == 0 or w == 0:
            K[i][w] = 0
        elif wt[i-1] <= w:
            K[i][w] = max(val[i-1] + K[i-1][w - wt[i-1]], K[i-1][w])
        else:
            K[i][w] = K[i-1][w]

for i in range(n + 1):
    print()
    for w in range(W + 1):
        print(K[i][w], end=" ")
    print()

res = K[n][W]
w = W
selected_items = []

for i in range(n, 0, -1):
    if res <= 0:
        break
    if res == K[i-1][w]:
        continue
    else:
        selected_items.append(wt[i-1])
    res = res - val[i - 1]
    w = w - wt[i - 1]

print("Maximum profit is", K[n][W])
print("Set of the combination for the maximum profit is:", selected_items)
end = time.time()
total = end - start
print("Total time taken : ", total, "ms")

# 3 4 5 6
# 2 3 4 5
# 5