## Euclid's Algorithm (method 1)
#import pandas as pd

def GCD(a, b):
    # Ensure a is the greater number
    if a < b:
        A = b
        B = a
    else:
        A = a
        B = b

    iter1 = 0
    #data = []  # List to store iteration data

    while B != 0:
        iter1 += 1
        R = A % B  # Find remainder
        
        #data.append({'Dividend': A, 'Divisor': B, 'Remainder': R})

        A = B  # Replace value
        B = R  # Replace remainder value with divisor

    #data.append({'Dividend': A, 'Divisor': B, 'Remainder': R})

    # Create DataFrame from the collected data
    #df = pd.DataFrame(data)

    # Print the DataFrame
    #print(df)
    print(f'The GCD of Number A and B is: {A}')
    print(f'Number of iterations: {iter1}')

    return A

# Example usage

GCD(3j ,2j)


