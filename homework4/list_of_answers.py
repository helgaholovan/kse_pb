def check(guess, w):
    result=[]; i=0
    while i<len(w):
        ch = guess[i]
        if ch==w[i]:
            result.append('correct')
        elif ch in w:
            result.append('present')
        else:
            result.append('absent')
        i+=1
    return result
    
