import time
import math

startTime = time.perf_counter()

'''
Thoughts - so we did a brute force attempt but we generally made all
the right observations, just forgot that primitive Pythagorean Triples
can be generated. This is at heart just a math problem so again, this
section will be pretty short. As a side note, the most efficient way I could
think about to test if a number is a square is to round the square root 
(no potential for floating point issues here) and then square it to check
for equality. This becomes increasingly more expensive for larger numbers. 

Run-time: 112.8735 seconds
Difficulty: Level 10
16177th person to solve this problem

Math notes - Triangle is x, x, x pm 1. First observation is that x must be odd.
If x is even, then the other side x -1 or x +1 is odd, and then we need to make
a Pythagorean triple with a fraction and an even value. This is impossible to 
then get an even value for the height which is needed to obtain integer area.

Therefore, x is odd. So, x - 1 or x + 1 is appropriately even and thus we can
think about a Pythagorean triple for x and (x-1)/2 or (x+1)/2. Generating
Pythagorean Triples by formula of (m^2 - n^2, 2mn, m^2 + n^2) and then checking
if we satisfy a relation of x and (x pm 1)/2 would suffice to do this efficiently.

'''
boundary = 10 ** 9 
output = 0

def square_test(n : int) -> bool:
    root = round(math.sqrt(n))
    return n == root * root

for x in range(3, int(boundary//(3.2)), 2):
    plus = 3 * x * x + 2 * x - 1
    minus = 3 * x * x - 2 * x - 1

    plus_perim = 3 * x - 1
    minus_perim = 3 * x + 1

    if square_test(plus) and plus_perim < boundary:
        output += plus_perim
        print(f"plus: {x}")

    if square_test(minus) and minus_perim < boundary:
        output += minus_perim
        print(f"minus: {x}")

print(f"Final output: {output}")

endTime = time.perf_counter()

elapsedTime = endTime - startTime
print(f"Runtime: {elapsedTime:.4f} seconds")