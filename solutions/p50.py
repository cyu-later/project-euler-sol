import time
import math

startTime = time.perf_counter()

"""
Thoughts - okay so we're a little rusty and haven't coded/done math
in a long time so giving some slack to myself here...

thanks to GPT there's a more efficient way to generate primes_to_n which
is basically done by checking less numbers i.e. in a previous problem
we were still trying to discard multiples of 4 when they were clearly all
discarded. 

Beyond that, we kind of just guess and checked for the question which isn't
great i.e. checking if 2 was the start, or if 3 was the start, and so on so forth.
More algorithmic/rigorous method I think is to just check by subtracting left/right
of the overall sum. I will come back to this question to implement the more algorithmic
form, but for now I'm ready to explore some new problems.

Run-time: 0.3714 seconds
Difficulty: 3 (they changed it in the time we left...)

Math notes: I don't think there's any super special theorem about consecutive primes
adding to a prime. I see a recent arxiv paper by Tolla about a conjecture on
the sum of consecutive primes that says for any prime number, there exists at
least one odd sum of consecutive primes that is prime, but that's about it. It seems
there's still a lot more to understand about primes...

"""
def primes_to_n(n: int) -> list:
    
    all = {x for x in range(2, n)}

    for i in range(2, int(math.sqrt(n)) + 1):

        if i not in all:
            continue

        j = i * i
        while j < n:
            all.discard(j)
            j += i
    
    return all

boundary = 1000000
primes_set = primes_to_n(boundary)
primes_list = sorted(primes_set)
curr = 0
max_prime = 0

for prime in primes_list[3:]:
    curr += prime
    if curr in primes_set:
        
        max_prime = max(max_prime, curr)
        print(f"new max: {max_prime}")

print(max_prime)
print(curr)

endTime = time.perf_counter()

elapsedTime = endTime - startTime
print(f"Runtime: {elapsedTime:.4f} seconds")