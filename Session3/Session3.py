def fibonnaci(num):
    fibonnaci = [1,1]
    for number in range(100):
        while fibonnaci[-1] < num:
            if number < 2:
                fibonnaci.append(number)
            else:
                fibonnaci.append(fibonnaci[number-2]+fibonnaci[number-1])
    return fibonnaci