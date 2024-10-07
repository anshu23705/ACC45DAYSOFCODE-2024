def can_measure_weight(W, X, Y, Z):
    # Check if the weight W is equal to any of the weights X, Y, or Z
    # If it is, we can measure the weight exactly, so return "YES"
    if W == X or W == Y or W == Z:
        return "YES"
    
    # Check if the weight W can be expressed as a sum of X and one of Y or Z
    # If W - X is equal to Y or Z, we can measure the weight exactly, so return "YES"
    if W - X >= 0 and (W - X == Y or W - X == Z):
        return "YES"
    
    # Check if the weight W can be expressed as a sum of Y and one of X or Z
    # If W - Y is equal to X or Z, we can measure the weight exactly, so return "YES"
    if W - Y >= 0 and (W - Y == X or W - Y == Z):
        return "YES"
    
    # Check if the weight W can be expressed as a sum of Z and one of X or Y
    # If W - Z is equal to X or Y, we can measure the weight exactly, so return "YES"
    if W - Z >= 0 and (W - Z == X or W - Z == Y):
        return "YES"
    
    # If none of the above conditions are true, we cannot measure the weight exactly, so return "NO"
    return "NO"

# Read in the number of test cases
T = int(input())

# Loop through each test case
for _ in range(T):
    # Read in the weights W, X, Y, and Z for this test case
    W, X, Y, Z = map(int, input().split())
    
    # Call the can_measure_weight function and print the result
    print(can_measure_weight(W, X, Y, Z))