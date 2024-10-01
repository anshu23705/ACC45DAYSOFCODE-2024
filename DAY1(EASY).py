# Read input values
A, B, C, X = map(int, input().split())

# Check if X is equal to A, B, or C
if X in [A, B, C]:
    print("Yes")
else:
    print("No")