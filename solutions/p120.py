import time
import math

startTime = time.perf_counter()

'''
Thoughts - confused by the difficulty here...not much to note here.
First try!

Run-time: 0.0003 seconds
Difficulty: Level 3
16895th person to solve this problem

Math notes - Everything just boils down to whether a is odd or even.
When we look at (a + 1)^n + (a - 1)^n, when n is even then taking it
modulo a^2 just gives 2 and it's pretty clear to see that this is never
going to be the max modulo a^2. So, just take n to be odd. 

Then, varying n means that our possible modulo a^2 are 2a, 6a, 10a ...
i.e. 2 * odd * a. If a is odd, then clearly the max will be a^2 - a
because eventually 2 * odd will be -1 mod a for some odd number. This
is like a scuffed Chinese Remainder Theorem application. On the other hand,
if a is even, then 2 * odd can only be -2 mod a. So, the max would be
a^2 - 2a. As such, we add a^2 - (2 - a % 2) * a for every a. 

'''

# 2 * (1, 3, 5, 7, ...) mod a
# if a is odd, then we're always good
# if a is even though, say a is 4
# we need smth mod 16. 2a * (1, 3, 5, 7), well this would only be 8. 

# how about 6. something mod 36.
# 12 * (1, 3, 5, 7) --> we can get 24
# probably just one less than 2a 

output = 0

for i in range(3, 1001):
    output += (i **2 - (2 - (i % 2)) * i)

print(f"Final output: {output}")

endTime = time.perf_counter()

elapsedTime = endTime - startTime
print(f"Runtime: {elapsedTime:.4f} seconds")