n=int(input()) # number of competitors
for i in range(n): 
    l=[int(x) for x in input().split()]
    t=l.count(1) # number of 1's in l = number of questions solved 
    if t==0:
        print("Beginner")
    if t==1:
        print("Junior Developer")
    if t==2:
        print("Middle Developer")
    if t==3:
        print("Senior Developer")
    if t==4:
        print("Hacker")
    if t==5:
        print("Jeff Dean")
        
