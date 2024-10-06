t=int(input()) # number of test case
for _ in range(t):
    x , y= map(int , input().split())
    # calculating the maximum number of months
    max_month = y//x-1
    # if max months = 0 or -ve , output will be 0
    if max_month <= 0:
        print(0)
    else:
        print(max_month)
        # run in terminal 