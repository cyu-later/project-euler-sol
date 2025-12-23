import math
import time

"""
Thoughts - brute force is generally fine when you 
identify an abundant one, you can then find 
any one thats the sum by adding it to all 
the other found abundant ones and you work up monotonically

Initially made a mistake in abundant defn where
we made 4 be abundant because we were double-counting
by adding both n//i and i. sqrt(n) decreases runtime than
going to n//2 though. 

Runtime: 2.1444
Math notes: every multiple of a perfect number is abundant
so e.g. multiples of 6 would all be abundant. Wikipedia says
best bound atm is 20161 i.e. every integer larger than this
can be written as sum of 2 abundant numbers
"""


def abundant(n : int) -> bool:
    total = 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            total += i
            if n//i != i:
                total += (n // i)

    return total > n

start_time = time.perf_counter()

abundant_set = set()
sum_abundant_set = set()

for i in range(1, 28124):
    if abundant(i):
        abundant_set.add(i)
    
        for abun in abundant_set:
            if abun + i <= 28123:
                sum_abundant_set.add(abun + i)
    
    
total_sum = sum(range(1, 28124))
print(f"Final Answer: {total_sum - sum(sum_abundant_set)}")

end_time = time.perf_counter()
elapsed_time = end_time - start_time
print(f"Program runtime: {elapsed_time:.4f} seconds")