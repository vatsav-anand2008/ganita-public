import time
import math
import csv
import statistics
from tqdm import tqdm
import numpy as np
import os 
import sys      
# Add the parent directory of 'ganita' to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))
from ganita.lilavati.squares import lilavati_square_v2 as lilavati_square
def karatsuba_square(n):
    if n < 10:
        return n * n
    
    m = len(n)
    m2 = m // 2
    
    high, low = divmod(n, 10**m2)
    
    z0 = karatsuba_square(low)
    z2 = karatsuba_square(high)
    z1 = karatsuba_square(high + low) - z2 - z0
    
    return (z2 * 10**(2*m2)) + (z1 * 10**m2) + z0

def multiplication_square(number):
    return number * number

def exponentiation_square(number):
    return number ** 2

def pow_square(number):
    return pow(number, 2)

def math_pow_square(number):
    return math.pow(number, 2)

def time_function(func, number, iterations=10):
    times = []
    for _ in range(iterations):
        start_time = time.time()

        result = func(number)
        end_time = time.time()
        times.append(end_time - start_time)
    return result, statistics.mean(times), statistics.stdev(times)

def generate_number(digits):
    #using string
    #return int(''.join(str(i % 10) for i in range(digits)))
    #using number
    return sum(((i % 10) * 10**i for i in range(digits)))

def generate_number_as_string(digits):
    #using string
    return ''.join(str(i % 10) for i in range(digits))


def main():
    methods = [
        ("Lilavati's method", lilavati_square),
        ("Karatsuba multiplication", karatsuba_square),
        ("Simple multiplication", multiplication_square),
        ("Exponentiation", exponentiation_square),
        ("Pow function", pow_square),
        ("Math.pow function", math_pow_square)
    ]

    # Generate 100 evenly spaced digit counts between 210000 and 1000000
    digit_counts = [round(x) for x in np.linspace(1, 100, 1)]

    # Dictionary to keep track of which methods have failed
    method_failed = {method_name: False for method_name, _ in methods}

    with open('square_calculation_results.csv', 'w', newline='') as csvfile, \
         open('method_failures.csv', 'w', newline='') as failure_file:
        csvwriter = csv.writer(csvfile)
        failure_writer = csv.writer(failure_file)
        
        csvwriter.writerow(['Digits', 'Method', 'Result Length', 'Mean Time', 'Standard Deviation'])
        failure_writer.writerow(['Digits', 'Method', 'Error'])

        for digits in tqdm(digit_counts):
            number_as_string = generate_number_as_string(digits)
            number_as_int = generate_number(digits)

            for method_name, func in methods:
                if not method_failed[method_name]:
                    try:
                        if method_name in ["Lilavati's method", "Karatsuba multiplication"]:
                            result, mean_time, std_dev = time_function(func, number_as_string, iterations=2)
                        else:
                            result, mean_time, std_dev = time_function(func, number_as_int, iterations=2)
                        result_length = len(str(result))
                        csvwriter.writerow([digits, method_name, result_length, mean_time, std_dev])
                    except Exception as e:
                        method_failed[method_name] = True
                        failure_writer.writerow([digits, method_name, str(e)])

    print("Experiment completed. Results saved in 'square_calculation_results.csv'")
    print("Failure log saved in 'method_failures.csv'")

# Set the limit to 0 to disable it entirely
sys.set_int_max_str_digits(0)

if __name__ == "__main__":
    main()