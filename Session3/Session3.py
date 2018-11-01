def fibonnaci_fun(highest):
    fibonnaci = [0,1]
    while fibonnaci[-2]+fibonnaci[-1] < highest:
        fibonnaci.append(fibonnaci[-2]+fibonnaci[-1])
    return fibonnaci 