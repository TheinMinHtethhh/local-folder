def star(n):
    
    for i in range(n):
        for j in range(i,n):
            print(' ',end='')
        for h in range(i):
            print('*',end='')
        for g in range(i+1):
            print('*',end='')
        print()
    for i in range(n):
        for j in range(i+1):
                print(' ',end='')
        for h in range(i,n-1):
                print('*',end='')
        for g in range(i,n):
                print('*',end='')
        print()
star(6)