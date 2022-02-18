def make_ascending_sorted_array(size):
    a = []
    for i in range(size):
        a.append(i)

    return a

# assume it takes in list of a size that is a power of two
def wc_merge(wc, start, mid, stop):
    wc_array = []
    i = start
    j = mid + 1
    choose_from_first_array = False
    
    while i <= mid and j <= stop :
        if choose_from_first_array == True :
            wc_array.append(wc[i])
            i += 1
            choose_from_first_array = False
        else:
            wc_array.append(wc[j])
            j += 1
            choose_from_first_array = True

    # Copy any remaining elements
    # Only one will execute
    while i <= mid :
        wc_array.append(wc[i])
        i += 1
    while j <= stop :
        wc_array.append(wc[j])
        j += 1

    # Copy sorted array back to original
    for num in wc_array :
        wc[start] = num
        start += 1
    
    return

def wc_mergesort_divide(wc, start, stop):
    # base case
    if stop - start < 1 :
        return

    mid = (start + stop)//2
    # divide left and right side till base case
    wc_mergesort_divide(wc, start, mid)
    wc_mergesort_divide(wc, mid + 1, stop)

    # merge and jumble
    wc_merge(wc, start, mid, stop)

    return

def worst_case_mergesort(size):
    wc = make_ascending_sorted_array(size)

    wc_mergesort_divide(wc, 0, len(wc)-1)

    return wc

## WRITE CODE HERE TO GENERATE WORST CASE and AVERAGE CASE INPUTS/PLOT
## You may cut and paste from code we provided or directly call them
size = 8
wc = worst_case_mergesort(size)
print(wc)