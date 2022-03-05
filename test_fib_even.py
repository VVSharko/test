def fib_even(n):
    if not isinstance(n, int):
        raise TypeError
    fib_list = []
    counter = 0
    while counter < n:
        counter += 1
        if counter > 2:
            new_fib = 4*fib_list[counter-2] + fib_list[counter-3]
            fib_list.append(new_fib)
            pass
        elif counter == 1:
            fib_list.append(0)
        elif counter == 2:
            fib_list.append(2)
    return fib_list
    
