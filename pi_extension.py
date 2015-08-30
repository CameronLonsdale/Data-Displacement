# Following Code to calculate digits of Pi was written by 
#"Balazs Rostas : MrBlaise"
#https://github.com/MrBlaise/learnpython/blob/master/Numbers/pi.py

# Find PI to the Nth Digit
# Have the user enter a number 'n'
# and print out PI to the 'n'th digit

def calcPi(limit):  # Generator function
    #Prints out the digits of PI
    #until it reaches the given limit

    q, r, t, k, n, l = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
        if 4 * q + r - t < n * t:
            # yield digit
            yield n
            counter += 1
            nr = 10 * (r - n * t)
            n = ((10 * (3 * q + r)) // t) - 10 * n
            q *= 10
            r = nr
        else:
            nr = (2 * q + r) * l
            nn = (q * (7 * k) + 2 + (r * l)) // (t * l)
            q *= k
            t *= l
            l += 2
            k += 1
            n = nn
            r = nr