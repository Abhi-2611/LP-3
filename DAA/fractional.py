class Item:
    def __init__(self, profit, weight):
        self.profit = profit
        self.weight = weight

def knapsack(w, arr):
    arr.sort(key=lambda x: (x.profit / x.weight), reverse=True)
    final = 0.0
    for item in arr:
        if item.weight <= w:
            w -= item.weight
            final = final + item.profit
        else:
            final += item.profit * w / item.weight
            break
    return final

if __name__ == "__main__":
    import time
    
    w = float(input("Enter the knapsack's weight capacity: "))
    n = int(input("Enter the number of items: "))
    arr = []
    
    for i in range(n):
        profit = float(input(f"Enter profit for item {i + 1}: "))
        weight = float(input(f"Enter weight for item {i + 1}: "))
        arr.append(Item(profit, weight))
    
    start = time.time()
    print("Maximum profit:", knapsack(w, arr))
    end = time.time()
    total = end - start
    print("Total time taken :", total, "ms")
    
    # 50
    # 60 10
    # 100 20 
    # 120 30 