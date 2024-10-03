# Number of cases
T = int(input())
for _ in range(T):
    N , X = map(int , input().split()) #N - length of array A, X - initial number of people
    A = list(map(int , input().split())) # Array A of events
    current_people = X # initial number of people
    max_people = X # initalia maximum is X
    for event in A:
        if event >=0:
            current_people += event #people entered the room
        else:
            current_people += event #people left the room
            #final maximim number of people 
            if current_people > max_people:
                max_people = current_people
                
                print(max_people) #print the maximum number of people in the room