import time
import math

startTime = time.perf_counter()


"""
Thoughts - okay so to be honest, I did use GPT to give a slight hint
and I guess I never thought to consider that this would just be
a number theory question and not DP or leetcode esque. So my
fault for not being more open-minded. Coding up the math was a slight
headscratcher but pretty straightforward after just hashing out the
exact variables/numbers.

Run-time: 0.0004 seconds
Difficulty: Level 4
20860th person to solve this problem

Math notes: The question revolves around Pell equations and this is a huge 
throwback to when I took Quadratic Forms (MAT419). The equation boils down to
(2n-1)^2 - 2(2k-1)^2 = -1 after completing the square, and the general
form is x^2 - 2y^2 = -1. We can observe that (1,1) is the "simplest" integral
solution. We can factorize this as (x - y sqrt(2))(x + y sqrt(2)) = -1, and
the cool thing is that -1 raised to any odd number is still -1! Therefore,
we can generate new solutions by just raising both sides to odd powers.

The idea is that raising to the next power generates new solutions because
the (x - y sqrt(2))^k and (x + y sqrt(2))^k will be a - bsqrt2 and a + bsqrt2
respesctively since the sqrt2 terms all collect together and it's just a matter
of sign within the binomial expansion. Therefore, they will need be a new 
solution to the Pell equation. It is somewhat assumed that these are the only
solutions i.e. you won't be able to find any other solution that doesn't match
(1 - sqrt(2))(1 + sqrt(2)) to some odd power.

From here, we simply have that 2n - 1 = x so n = (x + 1) / 2 and also
k = (y + 1) / 2. So, we simply loop through consecutive odd powers until
we reach that n > 10 ** 12, and then we can return the associated k value.

"""


# n^2 - n = 2k^2 - 2k
# n^2 - n + 1/4 = 2k^2 - 2k + 1/4 + 1/4 - 1/4
# (n-1/2)^2 = 2(k - 1/2)^2 - 1/4
# (2n -1)^2 - 2(2k-1)^2 = - 1
# n = 4
# 7^2 - 2 * 5^2 = -1
# n = 21
# x^2 - 2y^2 = -1
# 7^2 - 2 * 5^2 = -1
# 41^2 - 2 * 29^2 = -1
# (x - y sqrt(2))(x + y sqrt(2))) = -1 oh so cube it??? oh and then separate?
# (1 - sqrt(2))^3 = 1 - 3sqrt(2) + 6 - 2sqrt(2) = 7 - 5sqrt(2)
# so basically 2n -1  = x^3 + 6y^2 and the other one is 2y^3 + 3xy
# (x - ysqrt(2))^5   (x + y sqrt(2))^5 = -1


boundary = 10 ** 12
x = 1
y = 1
k = 1
n = 0

# expand (x + ysqrt(2))^k
# x^k + x^k-1 * y * sqrt(2) * k-1
def binomial_expand(x, y, k):
    nx = 0
    ny = 0
    real = True
    
    for i in range(k, -1, -1):
        if real:
            nx += (x ** i) * (y ** (k - i)) * (2 ** ((k-i)//2)) * math.comb(k,i)
            real = False
        else:
            ny += (x ** (i)) * (y **(k-i)) * (2 ** ((k-i)//2)) * math.comb(k,i)
            real = True

    return [nx, ny]

while n < boundary:
    x,y = binomial_expand(1, 1, k)

    n = (x + 1)//2
    k += 2
    print(n)

print((y+1)//2)

endTime = time.perf_counter()

elapsedTime = endTime - startTime
print(f"Runtime: {elapsedTime:.4f} seconds")