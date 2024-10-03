t = int(input())  # Number of test cases
for _ in range(t):
    X, Y = map(int, input().split())
    
    # Case 1: Solve A first, then B
    points_case1 = (500 - 2*X) + (1000 - 4*(X + Y))
    
    # Case 2: Solve B first, then A
    points_case2 = (1000 - 4*Y) + (500 - 2*(X + Y))
    
    # Output the maximum of the two
    print(max(points_case1, points_case2))
