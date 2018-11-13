def fibonnaci_fun(highest):
    fibonnaci = [0,1]
    while fibonnaci[-2]+fibonnaci[-1] < highest:
        fibonnaci.append(fibonnaci[-2]+fibonnaci[-1])
    return fibonnaci 

def delduplicates_1(input_list):
    output_list = []
    for number in input_list:
        if output_list.count(number) == False:
            output_list.append(number)
    output_list.sort()
    return output_list
    
def delduplicates_2(input_list):
    return list(set(input_list))