from itertools import chain, product
import hashlib, base64



def bruteforce(charset, maxlength):
    return (''.join(candidate)
        for candidate in chain.from_iterable(product(charset, repeat=i)
        for i in range(maxlength, maxlength + 1))) // change to 0 if you want to increase characters, leave if you want only this specific length

        
brutelist = list(bruteforce('abcdefghijklm', 9))

