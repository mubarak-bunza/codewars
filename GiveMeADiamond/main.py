def diamond(n):
    diamond = ''
    print(n)
    if n%2 == 0 or n < 0:
        return None
    else:
        starplus = 1
        starntive = n
        space = n//2
        for i in range(n+1):
            if i<(n//2):
                diamond += (space*' '+'*'*starplus+'\n')
                starplus += 2
                space -= 1 
            elif i>(n//2):
                diamond += (space*' '+'*'*starntive+'\n')
                starntive -= 2 
                space += 1
    return diamond