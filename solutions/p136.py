import time
import math

"""
Thoughts - this ends up being more of a math question
than a coding question. For kicks, I tried a brute force
approach and it took a whopping 1324.5159 seconds i.e. 
22 minutes...turns out with some helpful math it just
reduces to finding primes under n and primes that are
3 mod 4. See below for more details!

Runtime: 22.3091 seconds
Difficulty: 50%

Math notes: So the proof is that the only feasible n
are n that is 1) prime and 3 mod 4 2) 4 * prime and 4
or 3) 16 * prime and 16. First, notice that we can set
x = a + d, y = a, z = a - d for some a > d (positive int)
From there, simplifying shows that a(4d - a) = n. 

1) quadratic residues show that if n is odd, then n
must be 3 mod 4 from original expression that 
n = x^2 - y^2 - z^2. From there, notice then that if
n is 3 mod 4, and if its prime, then either a = 1, but
this can't happen for d < d. So, a = n is the only sol.
If n is composite (and 3 mod 4), then a = n still works. 
But, there is some a_1 a_2 = n where a_2 > a_1, and no
matter if a_2 is 3 or 1 mod 4, there exists a good d.

for 2) 3). These follow similarly from part 1) except
now things are even. The idea remains the same from
keeping track of the prime factors of n.

"""

startTime = time.perf_counter()

def primes_to_n (n:int) -> list:
    onePrime = [False] * n
    threePrime = [False] * n
    isPrime = [True] * n
    isPrime[0] = False
    isPrime[1] = False
    # for our purposes, this is fine
    # doesn't work for smth like 30
    isPrime[-1] = False
    idx = 2
    while idx < n:
        if isPrime[idx]:
            for mult in range(2, n// idx + 1):
                if idx * mult < n:
                    isPrime[idx * mult] = False
        idx += 1
        while not isPrime[idx]:
            idx += 1
            if idx == n:
                break
    for i in range(n):
        if i % 4 == 1 and isPrime[i]:
            onePrime[i] = True
        elif i %4 == 3 and isPrime[i]:
            threePrime[i] = True
    
    return isPrime, onePrime, threePrime

def valid_rep(n:int, a: int):
    four_d = n//a  + a
    if four_d % 4 == 0 and four_d//4 < a:
        return True
    
    return False

# 4 times prime is chill, what about 16 times, 4 * prime, thats also fine
# so only 16 times as well okay
# only 3 mod 4 though

# x = a + d, y = a, z = a - d
def singleton_diff(boundary: int) -> int:
    isPrime, _, threePrime = primes_to_n(boundary)

    return (sum(threePrime) - 2) + (sum(isPrime[:boundary//4]) + 1) + (sum(isPrime[:boundary//16]) + 1)

boundary = 5* (10 **7)

print(f"Boundary: {boundary}")
print(f"Total count: {singleton_diff(boundary)}")
endTime = time.perf_counter()
elapsedTime = endTime - startTime

print(f"Runtime: {elapsedTime:.4f} seconds")