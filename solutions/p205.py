import time
import math
import numpy as np
from numpy.polynomial import polynomial as P

startTime = time.perf_counter()

'''
Thoughts - translating probability into code. I couldn't think of
a good way to do the product of the generating functions (elaborated
in math section) although I had considered some kind of defaultdict, 
but I just ended up defaulting to a convenient numpy submodule...
The idea here is that we can construct a prefix array of Colin's 
coefficients, and then we can get all the possibile winning
configurations by taking Peter's probability he gets one value and then 
the smaller value in Colin's prefix array. 

Run-time: 0.0001 seconds
Difficulty: Level 3
17566th person to solve this problem

Math notes - We can model the outputs of the dice results using this
approach called generating functions which effectively just mean
polynomials here. Peter's probability distribution is modeled by the
coefficients of (x + x^2 + x^3 + x^4)^9 and Colin is similarly modeled
by (x + x^2 + ... x^6)^6. Then, we can do binomial expansions to get the
overall probabilities and then in theory, you can just manually compute out
all the winning configurations for Peter.

As a side note, adding a lot of dices generally leads to a normal distribution
for the sum. If we just assume the CLT here then we have approximate dist of:
Peter: N(22.5, 11.25)
Colin: N(21, 17.46)
In this way, it generally makes sense that Peter is favored to win a bit more
because it has more mass concentrated around a larger mean. 

'''


# we might want to compute unnormalized ways of getting things
# generating functions??
# probability of getting 36
# (x + x^2 + x^3 + x^4)^9
# (x + x^2 + x^3 + x^4 + x^5 + x^6)^6

# for getting something in the above one
# 

output = 0

peter = [0, 1, 1, 1, 1]
colin = [0, 1, 1, 1, 1, 1, 1]

peter_coef = P.polypow(peter, 9)
colin_coef = P.polypow(colin, 6)

colin_pref = [colin_coef[0]]
for coef in colin_coef[1:]:
    colin_pref.append(colin_pref[-1] + coef)

cumulative_prob = 0
for i in range(1, 37):
    cumulative_prob += (peter_coef[i] * colin_pref[i-1])

output = round(cumulative_prob/((4 ** 9 )* ( 6 ** 6) ), 7)


print(f"Final output: {output}")

endTime = time.perf_counter()

elapsedTime = endTime - startTime
print(f"Runtime: {elapsedTime:.4f} seconds")