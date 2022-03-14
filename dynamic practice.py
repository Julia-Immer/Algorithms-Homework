def minSubsetDifference_recursive(N, s_list):
    min_diff = N
    differences = []

    if N == 0 :
        return 0
    elif N < 0 :
        return 999999999
    
    for i in range(len(s_list)) :
        if N - s_list[i] > 0 :
            lst_sofar = s_list[:]
            lst_sofar.pop(i)
            differences.append(minSubsetDifference_recursive(N - s_list[i], lst_sofar[:]))
        else :
            differences.append(999999999)
    min_diff = min(differences)
    return min_diff






def minCoursesWithEnergyBudget_Memoize(e, n):
    level_jumps = [1, 4, 5, 11]
    energy_consumed = [1, 2, 3, 7]
    j = n - 1 # start at n - 1 since j = n takes 0 courses to get to
    k = e - 1 # our starting energy
    memo =  [[0]*(e+1)]*(n+1) # make the memo table with default values 0

    while j >= 1 :
        while k > 0 :
            options = [999999999]
            for i in range(len(level_jumps)) : # try each level
                if k + energy_consumed[i] > 0 : # go until energy is consumed
                    # make sure you don't hit bad levels
                    if j + level_jumps[i] < n  and ((j + level_jumps[i])%7 != 2) : # avoid the bad levels
                        options.append(memo[j + level_jumps[i]][k + energy_consumed[i]] + 1)
                    elif j + level_jumps[i] == n :
                        options.append(memo[j + level_jumps[i]][k + energy_consumed[i]] + 1)
                    else :
                        options.append(999999999)
                else :
                    options.append(999999999)
                
            memo[j][k] = min(options)
            k -= 1

        j -= 1

    return memo


# test code do not edit
print(minCoursesWithEnergyBudget_Memoize(25, 10)) # must be 2
print(minCoursesWithEnergyBudget_Memoize(25, 6)) # must be 1
print(minCoursesWithEnergyBudget_Memoize(25, 30)) # must be 5
print(minCoursesWithEnergyBudget_Memoize(16, 30)) # must be 7
print(minCoursesWithEnergyBudget_Memoize(18, 31)) # must be 7
print(minCoursesWithEnergyBudget_Memoize(22, 38)) # must be 7
print(minCoursesWithEnergyBudget_Memoize(32, 55)) # must be 11
print(minCoursesWithEnergyBudget_Memoize(35, 60)) # must be 12




# def minCoursesForJane_Memoize(n): 
#     j = n - 1
#     memo = [0] * (n + 1) # make the memo table with default values 0
#     level_jumps = [1, 4, 5, 11]
#     options = []

#     # start at j = n - 1 and walk down to 1 to fill table
#     # how many jumps (courses), does it take for Jane to 
#     # get to level n from j? Each memo[j] answers that question
#     # Jane starts at level 1, however so we return memo[1]
#     while j >= 1 :
#         options = [999999999]
#         for jumps in level_jumps :
#             if j + jumps <= n :
#                 options.append(memo[j + jumps] + 1)
#         memo[j] = min(options)
#         j -= 1

#     print(memo)
#     return memo[1]


# def minCoins_memoize_1(x, lst):
#     T = [0]*(x+1) # make a list of all zeros of size x + 1
#     for i in range(1,x+1):
#         opts = [1 + T[i - cj] for cj in lst if (i - cj >= 0)]
#         opts.append(10000000) # so that the list is not empty. Or else, the next line will throw an exception
#         T[i] = min(opts)
#     return T[x]

# def minCoins_1(x, lst):
#     T = [0] * (x+1) # memo table
#     S = [-1]* (x+1) # best current/immediate decision
#     coins_used = []
#     for i in range(1,x+1):
#         opts = [ (1 + T[i - cj], cj)  for cj in lst if i - cj >= 0]
#         opts.append((1000000000, -1)) # Append + infinity to avoid min(..) raising an exception in the next line
#         T[i], S[i] = min(opts)
#     # NOW RECOVER the list of coins by using the S table.
#     value_left = x
#     while value_left > 0:
#         coins_used.append(S[value_left])# append the immedidate decision
#         value_left = value_left - S[value_left] # update the amount left
#     assert value_left == 0
#     return T[x], coins_used

# ## Test Code: Do not edit
# print(minCoursesForJane_Memoize(9)) # should be 2
# print(minCoursesForJane_Memoize(13)) # should be 2
# print(minCoursesForJane_Memoize(19)) # should be 4
# print(minCoursesForJane_Memoize(34)) # should be 3
# print(minCoursesForJane_Memoize(43)) # should be 5

