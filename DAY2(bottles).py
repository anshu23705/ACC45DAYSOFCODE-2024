T = int(input())

for _ in range(T):
  B1 , B2 , B3 = map(int,input().split())
  empty_bottles = [B1 , B2 , B3].count(0)
  if empty_bottles >= 2:
    print("Water filling time")
  else:
    print("Not now")
    # Run the code in terminal