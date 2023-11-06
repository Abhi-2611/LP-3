def fibonacci_of(n):
  if n in {0, 1}:
        return n
  return fibonacci_of(n - 1) + fibonacci_of(n - 2)

def Fibonacci(n):
    if n < 0 :
        print("Incorrect input")
    elif n == 0 :
        return 0 
    elif n == 1 or n == 2 :
        return 1
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)    
import time
start = time.time()
nterms = int(input("Enter the number of terms: "))
for i in range(nterms) :
    print(Fibonacci(i), end = " ")
print()
end = time.time()
total = end - start
print("Total time taken : ", total, "ms")