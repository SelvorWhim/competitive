# idea: unfairness will be minimized for a subset that's sequential in a sorted version of the list,
# and it's much easier to check a sorted list for the best subsequence than all subsets
# also, in subsequence of sorted arr, min will be the first and max will be the last

def min_unfairness(arr,k):
    if k==0 or len(arr)==0:
        return 0
    arr.sort() # mutates. Non mutating version will take extra space
    return min((arr[i+(k-1)] - arr[i]) for i in range(len(arr)-(k-1)))
