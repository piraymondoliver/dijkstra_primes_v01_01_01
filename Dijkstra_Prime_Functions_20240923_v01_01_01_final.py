# Dijkstra_Prime_Functions_20240923_v01_01_01_final.py
# Author: Pi Raymond Oliver [https://www.github.com/piraymondoliver]
# Version: v01_01_01_final
# Date: 2024/09/23
# Credit to the great Edgsar Dijkstra for inspiration in regarding this implementation in Python of his nth prime function
# Source: [E.W. Dijkstra - Notes on Structured Programming] : [https://www.cs.utexas.edu/~EWD/ewd02xx/EWD249.PDF]

####
####
####
####
# function Dijkstra_nth_prime(N)
# returns the Nth prime (e.g, the first prime is 2, the second is 3, and so on and so forth)
def Dijkstra_nth_prime(N):
    # variables declaration:
        # variables
    cur_prime = 1               # current prime
    cur_square = 4              # current square
    cur_limit = 1               # current limit
        # lists
    primes_l = [2]              # Initialize first element of primes list to 2
    multiples_l = [0] * N       # Initialize '0' in every element of multiples list (N-elements)

    for i in range(2, N + 1):   # loop takes on values from 2 to N
        while True:
            cur_prime += 2
            if (cur_square <= cur_prime):
                multiples_l[cur_limit - 1] = cur_square
                cur_limit += 1
                cur_square = ((primes_l[cur_limit - 1])**2)

            k = 2
            BOOL_ISPRIME = True

            while (BOOL_ISPRIME and (k < cur_limit)):
                if (multiples_l[k - 1] < cur_prime):
                    multiples_l[k - 1] += primes_l[k - 1]
                BOOL_ISPRIME = (cur_prime != multiples_l[k- 1])
                k += 1

            if BOOL_ISPRIME:           # break condition from loop (if BOOL_ISPRIME is set to true; implements a do-while loop)
                break

        primes_l.append(cur_prime)     # append the nth prime to the list

    return cur_prime                   # return the value of the current prime through the function
####
####
####
####




####
####
####
####
# function Dijkstra_first_n_primes(N)
# returns the a list of N primes up to the Nth prime (e.g, the first prime is 2, the second is 3, and so on and so forth)
def Dijkstra_first_n_primes(N):
    # variables declaration:
        # variables
    cur_prime = 1               # current prime
    cur_square = 4              # current square
    cur_limit = 1               # current limit
        # lists
    primes_l = [2]              # Initialize first element of primes list to 2
    multiples_l = [0] * N       # Initialize '0' in every element of multiples list (N-elements)

    for i in range(2, N + 1):   # loop takes on values from 2 to N
        while True:
            cur_prime += 2
            if (cur_square <= cur_prime):
                multiples_l[cur_limit - 1] = cur_square
                cur_limit += 1
                cur_square = ((primes_l[cur_limit - 1])**2)

            k = 2
            BOOL_ISPRIME = True

            while (BOOL_ISPRIME and (k < cur_limit)):
                if (multiples_l[k - 1] < cur_prime):
                    multiples_l[k - 1] += primes_l[k - 1]
                BOOL_ISPRIME = (cur_prime != multiples_l[k- 1])
                k += 1

            if BOOL_ISPRIME:           # break condition from loop (if BOOL_ISPRIME is set to true; implements a do-while loop)
                break

        primes_l.append(cur_prime)     # append the nth prime to the list

    return primes_l                   # return the list of N primes through the function
####
####
####
####