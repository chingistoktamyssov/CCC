n = int(input())

k = 0

swifts = [int(x) for x in input().split()]
semaphores = [int(x) for x in input().split()]

swiftstotal = 0
semaphorestotal = 0

for i in range(n):
    swiftstotal += swifts[i]
    semaphorestotal += semaphores[i]

    if swiftstotal == semaphorestotal:
        k = i + 1

print(k)