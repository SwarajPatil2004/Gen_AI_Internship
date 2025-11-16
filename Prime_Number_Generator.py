# Get input
try:
    start = int(input("Enter range start: "))
    end = int(input("Enter range end: "))
    
    # Validate input (must be positive integers)
    if start <= 0 or end <= 0:
        print("Error: Both numbers must be positive integers.")
    elif start > end:
        print("Error: Start must be less than or equal to end.")
    else:
        # Find all prime numbers within the range (inclusive)
        primes = []
        for num in range(start, end + 1):
            if num < 2:
                continue
            is_prime = True
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    is_prime = False
                    break
            if is_prime:
                primes.append(num)
        
        # Display primes (10 numbers per line)
        if primes:
            print("\nPrime numbers in the range:")
            for i in range(len(primes)):
                print(primes[i], end=" ")
                if (i + 1) % 10 == 0:
                    print()
            print()
        else:
            print("No prime numbers found in the given range.")
            
except ValueError:
    print("Error: Invalid input. Please enter valid integers.")