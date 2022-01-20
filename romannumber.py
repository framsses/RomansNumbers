
# Define a list with tuples to filter different numbers
romanfilter = [(1000, 'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),
                (90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),
                (1,'I')]

# Define a function to convert arabic numbers to roman numbers
def integer_to_roman(number: int):

    # Define an string variable with an empty value for the roman number
    nroman = ''

    while 3999 > number > 0:
        
        for arabicf, romanf in romanfilter:

            while number >= arabicf:
                nroman += romanf
                number -= arabicf
    
    if number > 3999:
        return 'There was an error in the input'

    return nroman

# Define a function to convert roman numbers to arabic numbers
def roman_to_integer(roman: str):

    # Define an int variable with an empty value for the roman number
    number = 0
    attemps = 0

    while len(roman) > 0 and attemps != len(romanfilter):

        for arabicf, romanf in romanfilter:

            if roman[:2] == romanf:
                number += arabicf
                roman = roman[2:]
                attemps = 0
            elif roman[:1] == romanf:
                number += arabicf
                roman = roman[1:]
                attemps = 0

        attemps += 1 

    if (number == 0 and attemps == len(romanfilter)) or number > 3999:
        return  'There was an error in the input'   
    
    return number

def main():

    option = int(input('''Select an option:
1) Convert arabic number to roman number
2) Convert roman number to arabic number
3) Exit Program
> '''))

    while 1 <= option <= 3:

        if option == 1:
            # Introduce a integer number
            ninteger = int(input('\nIntroduce a number between 1 and 3999: '))

            # Set a roman number with the help of integer_to_roman function
            nroman = integer_to_roman(ninteger)

            # Print a roman number
            print(f'The roman number is: {nroman} \n')

            main()
        
        elif option == 2:
            # Introduce a string roman number 
            roman = input('\nIntroduce a roman number between I and MMMCMXCIX: ')

            # Set an arabic number with the help of a roman_to_integer function
            ninteger = roman_to_integer(roman.upper())
            
            #Print a arabic numebr
            print(f'The integer number is: {ninteger} \n')
        
            main()
        
        else:
    
            print('\nExit Successfully \n')
        
        break

if __name__ == '__main__':
    main()

