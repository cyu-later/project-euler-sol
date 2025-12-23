import time


"""

Thoughts - tried a brute force approach of just
doing i and j in ranges(1,10001) which gave a very
long solution. Realized that there's no need to go
further beyond 2 million so you can find a hard cut-off
for i, set j at i to begin with (no need to repeat symmetric
cases) and continue while finding the min-distance and 
associated area

Run-time: 0.0061 seconds
Math notes: the number of sub rectangles in a m x n
tile rectangular grid is C(m+1, 2) * C(n+1, 2). Intuitively,
m +1 lines create the m columns (or rows), and we pick two of them 
to select the columns included in our sub-rectangle. Likewise, 
pick 2 of the n + 1 lines that create the n rows (or columns) and
each combination gives a unique sub-rectangle i.e. a bijection!
"""


startTime = time.perf_counter()

def choose_two(n: int):
    return ((n+1) * (n)) // 2


min_dist = float('inf')
area, num_rect = 0, 0
constant = 2000000


# Rough boundary of when n * (n+1) //2 approx 2 million
for i in range(1, 4001):
    j = i
    while choose_two(i) * choose_two(j) < constant:
        comp = choose_two(i) * choose_two(j)
        if abs(comp - constant) < min_dist:

            min_dist = abs(comp - constant)
            num_rect = choose_two(i) * choose_two(j)
            area = i * j
        j += 1

print(f"Area: {area}")
print(f"Min-dist: {min_dist}")
print(f"Actual Num of Rectangles: {num_rect}")


endTime = time.perf_counter()
elapsedTime = endTime - startTime

print(f"Runtime: {elapsedTime:.4f} seconds")