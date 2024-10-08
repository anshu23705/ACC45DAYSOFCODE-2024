#loop through each case
for case in cases:
    # read the size of the array N
    N = read integer
    # read the array A
    A = read array of integers

    #  intialize a counter to count the number of odd elements in A
    odd_count = 0
    # loop through each element in A
    for i in range(N):
        # check if the element is odd
        if A[i] % 2 != 0:
            # increment the counter if the element is odd
            odd_count += 1
            # check if the count of odd elements is odd
            if odd_count % 2 != 0:
                # if the count is odd, print "YES"
                print "YES"
                # otherwise print NO
                print "NO"
