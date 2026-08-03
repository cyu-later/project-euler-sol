import time
import math

startTime = time.perf_counter()


"""
Thoughts - solved this one on our own!! I think it's interesting how normal 
math observations kinda need to be manipulated in a different way. This will
of course be explained in the maht section. Since the coding part had nothing
intensive to it, the bulk of notes will be in the math section.

Run-time: 0.0001 seconds
Difficulty: Level 4
11064th person to solve this problem

Math notes: So, we want to first notice that these hollow square laminae are
clearly numbers of form x^2 - y^2, but specifically where x - y is even in order
to have the even border. If this is the case and we denote x > y, then we have that
x = y + 2k. If we want to find n = x^2 - y^2 with valid representations, then
n = 4k^2 + 4ky = 4k(k + y). This implies that we can use k =1 to give a valid rep
for all multiples of 4 starting from 4, and then k = 2 gives a valid rep for multiples
of 8 starting from 16, and so forth. So, we just sum up n//(4 * i) - i and that's it.

"""

boundary = 1000000

def calculate_ways(n):
    output = 0
    
    i = 1
    
    while 4 * i * i <= n:
        output += (n//(4 * i) - i)
        i += 1

    return output

print(calculate_ways(boundary))


endTime = time.perf_counter()

elapsedTime = endTime - startTime
print(f"Runtime: {elapsedTime:.4f} seconds")