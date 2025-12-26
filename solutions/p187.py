import time
import math

'''
Thoughts - Merry Christmas! This was a struggle
to get done in a reaosnable runtime without tinier 
optimizations like multithreading which I think 
could marginally speed up things like finding primes. 
Turns out the double for loop doesn't end up being 
horrible as well in the semiprime + prime count. 

Runtime: 85.8976 seconds
Difficulty: 25%

Math-notes: The idea is that we just look at all
combos of prime * prime and then set each multiple
above to definitely not semiprime or prime. Kind
of its own sieve. 

'''

startTime = time.perf_counter()

def primes_to_n(n: int) -> set:
    
    all = {x for x in range(2, n)}

    for i in range(2, int(math.sqrt(n)) + 1):
        j = 2
        while j * i < n:
            all.discard(j * i)
            j += 1
    
    return all

# exclusive
def primes_count_to_n (n: int) -> set:
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
    
    return sum(isPrime)


def semiprime_and_prime(n: int) -> int:
    
    # iterate over each one
    primes = list(primes_to_n(int(math.sqrt(boundary)) + 1))
    all = [True] * n
    all[0] = False
    all[1] = False

    for i in range(len(primes)):
        for j in range(i, len(primes)):
            prime_one, prime_two = primes[i], primes[j]
            square = prime_one * prime_two
            j = 2
            while square * j < n:
                all[square * j] = False
                j += 1
    
    return sum(all)

boundary = 10**8

print(f"Final count: {semiprime_and_prime(boundary) - primes_count_to_n(boundary)}")

endTime = time.perf_counter()

elapsedTime = endTime - startTime

print(f"Run-time: {elapsedTime:.4f} seconds")