def add_res(guess, wl, result) :
    display=[]
    j=0
    while j<wl:
        s = guess[j]
        res = result[j]
        if res=='correct':
            display.append("["+s.upper()+"]")
        elif res=='present':
            display.append("("+s+")")
        else:
            display.append(" "+s+" ")
        j+=1
    return display