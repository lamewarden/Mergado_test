#!/usr/bin/python3
def super_prime(numb):
    """Wrapping function, which extrapolates Erathosthenes sieve forward and 
    checks resulting prime numbers for being palindroms.
    Such composition was selected, for being presise and much faster than a classic 
    Trial division test (where to check if N is prime we have to do N / every prime number from 2 to sqrt(N))

    Args:
        numb (int): Value for which we look next prime palindrom
    """
    
    def sieve_of_eratosthenes(numb):
        """Classic Erathosthenes sieve algorythm - can be found everhywhere.

        Args:
            limit (_type_): _description_

        Returns:
            _type_: _description_
        """
        primes = [True for i in range(numb+1)]
        p = 2
        while p**2 <= numb:
            if primes[p]:
                for i in range(p**2, numb+1, p):
                    primes[i] = False
            p += 1

        return [p for p in range(2, numb) if primes[p]]
    
    
    def rec_palinfrom(numb):
        """Simple palindrom checker, based on recursion"""
        numb = str(numb)
        if len(numb) <=1:
            return True
        elif numb[0] == numb[-1]:
            return rec_palinfrom(numb[1:-1])
        else:
            return False
    
    # Initial data type check:
    try:
        numb = int(numb)
    except ValueError:
        print("Input value is invalid")
        return
    else:
        pass
    
    
    limit = numb*2
    for lst in sieve_of_eratosthenes(limit):
        # to drop all primes less than numb at once
        if lst <= numb:
            pass
        elif rec_palinfrom(lst) is False:
            pass
        elif rec_palinfrom(lst) is True:
            return lst
        else:
            # if not found in this iteration, increasing limit X2and forward
            # - "expanding" the sieve there and trying again
            super_prime(limit)

if __name__ == "__main__":
    numb = input("Enter the number: ")
    result = super_prime(numb)
    print(result)
        