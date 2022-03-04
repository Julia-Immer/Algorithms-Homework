def minCoursesForJane_Memoize(n): 
    j = n - 1
    memo = [0] * (n + 1) # make the memo table with default values 0
    level_jumps = [1, 4, 5, 11]
    options = []

    # start at j = n - 1 and walk down to 1 to fill table
    # how many jumps (courses), does it take for Jane to 
    # get to level n from j? Each memo[j] answers that question
    # Jane starts at level 1, however so we return memo[1]
    while j >= 1 :
        options = [999999999]
        for jumps in level_jumps :
            if j + jumps <= n :
                options.append(memo[j + jumps] + 1)
        memo[j] = min(options)
        j -= 1

    print(memo)
    return memo[1]


def minCoins_memoize_1(x, lst):
    T = [0]*(x+1) # make a list of all zeros of size x + 1
    for i in range(1,x+1):
        opts = [1 + T[i - cj] for cj in lst if (i - cj >= 0)]
        opts.append(10000000) # so that the list is not empty. Or else, the next line will throw an exception
        T[i] = min(opts)
    return T[x]

def minCoins_1(x, lst):
    T = [0] * (x+1) # memo table
    S = [-1]* (x+1) # best current/immediate decision
    coins_used = []
    for i in range(1,x+1):
        opts = [ (1 + T[i - cj], cj)  for cj in lst if i - cj >= 0]
        opts.append((1000000000, -1)) # Append + infinity to avoid min(..) raising an exception in the next line
        T[i], S[i] = min(opts)
    # NOW RECOVER the list of coins by using the S table.
    value_left = x
    while value_left > 0:
        coins_used.append(S[value_left])# append the immedidate decision
        value_left = value_left - S[value_left] # update the amount left
    assert value_left == 0
    return T[x], coins_used

## Test Code: Do not edit
print(minCoursesForJane_Memoize(9)) # should be 2
print(minCoursesForJane_Memoize(13)) # should be 2
print(minCoursesForJane_Memoize(19)) # should be 4
print(minCoursesForJane_Memoize(34)) # should be 3
print(minCoursesForJane_Memoize(43)) # should be 5

