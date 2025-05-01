from time import *

def lilavati_square_v2(num_str):
    startTime=time()
    '''
    Lilavati's square method is a traditional Indian method for squaring numbers.
    It involves breaking down the number into its digits, squaring each digit, and
    then using these squares to form the final result.

    Args:
        num_str (str): A string representation of the number to be squared.

    Returns:
        int: The square of the input number.
    '''
    length = len(num_str)
    result = 0
    unit=1
    #loop from last digit to first digit
    for i in range(length-1, -1, -1):
        result+= int(num_str[i])**2 * unit
        temp_unit=unit
        for j in range(i-1, -1, -1):
            temp_unit=temp_unit*10
            result+= 2*int(num_str[i])*int(num_str[j]) * temp_unit
        unit*=100
    endTime=time()
    elapsedTime=endTime-startTime
    print('time:',elapsedTime)
    return result

def lilavati_square_v1(number):
    startTime=time()
    if number < 10:
        return number * number

    num_str = str(number)
    length = len(num_str)
    result = 0
    
    # Pre-calculate powers of 10
    powers_of_10 = [10 ** i for i in range(length)]

    

    for i, digit in enumerate(num_str):
        digit = int(digit)
        place_value = powers_of_10[length - i - 1]
        term = digit * place_value
        
        # Square of the term
        result += term * term
        
        # Cross products
        remaining = int(num_str[i+1:]) if i < length - 1 else 0
        result += 2 * term * remaining
    endTime=time()
    elapsedTime=endTime-startTime
    print('time:',elapsedTime)
    return result

#check the validity of the function in a main function
def main():
    print(lilavati_square_v1(123))
    print(lilavati_square_v2('123'))

if __name__ == "__main__":
    main()