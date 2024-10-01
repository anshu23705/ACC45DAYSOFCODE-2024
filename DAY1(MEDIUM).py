t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    freq ={}
    for num in a:
        if num in freq:
            freq[num]+=1
else:
        freq[num]=1
max_freq = max(freq.values())
print(n-max_freq)
    