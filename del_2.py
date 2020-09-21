def print_prime_factors(N): # ikke endre den linjen
    print('Input:', N)

    while N > 1:
        f = 2   #f = factor
        while True: 
            if N % f == 0:
                N //= f
                print(f)
                break
            f += 1
    
    
    
# ikke endre noe nedenfor
if __name__ == "__main__":
    print_prime_factors(10)
    print()
    
    print_prime_factors(27)
    print()
    
    print_prime_factors(28)
    print()
    
    print_prime_factors(53)
    print()
    
    print_prime_factors(14092020)
