def is_monopoly(profits):
    """
    Checks if there is a monopoly in the market based on the profits made by four companies.

    Args:
    profits (list): A list of four integers representing the profits made by companies A, B, C, and D.

    Returns:
    str: "YES" if there is a monopoly, "NO" otherwise.
    """
  
    for i in range(4):
        # Calculate the sum of profits made by all companies except the current company
        sum_others = sum(profits[:i] + profits[i+1:])
        # Check if the profit made by the current company is strictly greater than the sum
        if profits[i] > sum_others:
         return "YES"
    return "NO"

# Read the number of test cases
T = int(input())

# Process each test case
for _ in range(T):
    # Read the profits made by companies A, B, C, and D
    profits = list(map(int, input().split()))
    # Check if there is a monopoly and output the result
    print(is_monopoly(profits))
