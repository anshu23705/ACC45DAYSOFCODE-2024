def min_masks(N, A):
    # The function min_masks takes in two parameters: N, the total number of people in the city,
    # and A, the number of people already infected with the virus.
    
    # The goal is to find the minimum number of people that need to wear a mask to prevent the further spread of the virus.
    # Since the virus can only spread when an infected person comes into contact with a non-infected person and neither is wearing a mask,
    # we need to ensure that at least one person in each potential contact pair is wearing a mask.
    
    # To achieve this, we can make either all infected people wear masks or all non-infected people wear masks.
    # The minimum number of people that need to wear a mask is therefore the smaller of A (the number of infected people) and N-A (the number of non-infected people).
    return min(A, N-A)

# Read in the number of test cases
T = int(input())
# T is the number of test cases, and we will loop through each test case.

# Loop through each test case
for _ in range(T):
    # Read in the total number of people N and the number of infected people A for this test case
    N, A = map(int, input().split())
    
    # Call the min_masks function and print the result
    print(min_masks(N, A))
    # This will print the minimum number of people that need to wear a mask to prevent the further spread of the virus for this test case.