"""
Problem statement :

In a university, your attendance determines whether you will be allowed to attend your graduation ceremony. You are not allowed to miss classes for four or more consecutive days. Your graduation ceremony is on the last day of the academic year, which is the Nth day.
Your task is to determine the following:
1. The number of ways to attend classes over N days.
2. The number of ways that you will miss your graduation ceremony (which is the last day)

Represent the solution in the string format as "Answer of (2) / Answer of (1)", don't actually divide or reduce the fraction to decimal.

"""


N = int(input())

dp_arr = [[-1 for _ in range(5)] for _ in range(N+1)]
dp_arr2 = [[-1 for _ in range(5)] for _ in range(N+1)]


def find_total_ways(n=5, prev=4):
    if n == 0:
        return 1

    if dp_arr[n][prev] != -1:
        return dp_arr[n][prev]
    # prev depict number of leaves left in bank
    if prev == 1: # i can take 1 leave
        # so if i take leave then pass 0 (1 - 1) and
        # if i don't take leave then refresh bank with again 3 leaves left
        dp_arr[n][prev] = find_total_ways(n - 1, 3) + find_total_ways(n - 1, 0)

    elif prev == 0:
        # no leave left so have to be present
        dp_arr[n][prev]= find_total_ways(n - 1, 3)

    elif prev == 2:
        # 2 leaves left in bank, if take it pass 1 (2 - 1) else refresh bank
        dp_arr[n][prev]= find_total_ways(n - 1, 3) + find_total_ways(n - 1, 1)
    elif prev == 3:
        dp_arr[n][prev]= find_total_ways(n - 1, 3) + find_total_ways(n - 1, 2)
    else:
        # starting, so can do both
        dp_arr[n][prev] = find_total_ways(n - 1, 3) + find_total_ways(n - 1, 2)
    return dp_arr[n][prev]




def find_ways_miss_ceremony(n=5, prev=4):
    if n == 1 and prev != 0:
        return 1
    if n == 1 and prev == 0:
        return 0
    if prev == 1:
        dp_arr2[n][prev] = find_ways_miss_ceremony(n - 1, 3) + find_ways_miss_ceremony(n - 1, 0)
    elif prev == 0:
        dp_arr2[n][prev] = find_ways_miss_ceremony(n - 1, 3)
    elif prev == 2:
        dp_arr2[n][prev] = find_ways_miss_ceremony(n - 1, 3) + find_ways_miss_ceremony(n - 1, 1)
    elif prev == 3:
        dp_arr2[n][prev] = find_ways_miss_ceremony(n - 1, 3) + find_ways_miss_ceremony(n - 1, 2)
    else:
        dp_arr2[n][prev] = find_ways_miss_ceremony(n - 1, 3) + find_ways_miss_ceremony(n - 1, 2)
    return dp_arr2[n][prev]


numerator = find_ways_miss_ceremony(N, 4)
denominator = find_total_ways(N, 4)

print(f'{str(numerator)}/{str(denominator)}')
