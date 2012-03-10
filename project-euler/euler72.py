import time

start = time.time()

LIMIT = 10**6+1

tot = [1]*(LIMIT)

for i in range(2, LIMIT):
    if tot[i] == 1:
        for j in range(i, LIMIT, i):
            tot[j] *= i - 1
            k = j / i
            while k % i == 0:
                tot[j] *= i
                k /= i

tot[0] = 0

print sum(tot)
print time.time() - start


