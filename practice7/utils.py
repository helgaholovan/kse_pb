def is_prime(n):
    l = int(n/2+1)
    for i in range(2, l) :
        if n%i==0 :
            goal =  False
        else :
            goal = True
    return goal
