numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
a = 0
for i in range(len(numbers)) :
    if numbers[i] != 1 :
        for j in range( numbers[i-1]) :
            if numbers[i] % (j + 1) == 0 :
                a= a + 1
        if a >= 2 :
            not_primes.append(numbers[i])
        else: primes.append(numbers[i])
        a = 0
print (not_primes)
print (primes)
