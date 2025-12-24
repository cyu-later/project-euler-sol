import time

"""
Thoughts - turns out just adding in math
to the reasoning brought it down to reasonable time.
Will be elaborated on later, but I couldn't think of
a better way other than just iterating through everything
from 1 to 10 mil. Overall a pretty good problem. Turns out
trimming zeros from integers speeds things up a LOT since
you're immediately reducing to cases you've probably seen.

Runtime: 6.9622 seconds
Math notes: Zeros don't contribute to total sum and bc we
iterate in order from 1 to 10mil, then we'll likely encounter
upon the no-zero number. Also, as long as its on the path from
x to 1 or 89, then we can include those in our large sets.

"""

def digit_sum(n : int) -> int:
    total = 0

    while n > 0:
        total += (n % 10) ** 2
        n //= 10
    
    return total

def determine(n : int) -> tuple[bool, set]:
    output = {n}
    while n != 1 and n != 89:
        n = digit_sum(n)
        output.add(n)
    if n == 1:
        return (True, output)
    else:
        return (False, output)

def trim_zeros(n: int) -> int:
    string = sorted(str(n))
    idx = 0
    while string[idx] == '0':
        idx += 1

    return int("".join(string[idx:]))

startTime = time.perf_counter()


one_set = set()
en_set = set() # 89 set
boundary = 10000000
count = 0

i = 5005


for i in range(1, boundary):
    i = trim_zeros(i)
    if i in en_set:
        count += 1
    elif i in one_set:
        continue
    else:
        in_set, to_add = determine(i)
        if in_set:
            one_set.update(to_add)
        else:
            en_set.update(to_add)
            count += 1

endTime = time.perf_counter()

elapsedTime = endTime - startTime
print(f"Total count: {count}")
print(f"Runtime: {elapsedTime:.4f} seconds")