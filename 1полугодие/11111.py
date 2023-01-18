for A in range(1, 100000):
    i=True
    for x in range(1, 100000):
        if (x%2==0) <= (not x%3==0) or (x+A>=100):
            i=True
        else:
            i=False
            break
    if i==True:
        print(A)
        break
