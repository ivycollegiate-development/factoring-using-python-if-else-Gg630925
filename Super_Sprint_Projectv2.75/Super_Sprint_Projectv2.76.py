#List all of the factors of a value 
def list_factors(n):
    # Explain the line of code below
    return [i for i in range (1, n+1) if n % i == 0]
    # Comment your explination here

    if _name_ == '_main_': # Checks to 
    #Ask the
    user_input = input('Pleace enter a number here: ')
    #
    nubmer = int(user_input)
    #
    if nubmer <= 0:
        Print('Please enter a positive number.')
    else:
        #
        factors = list_factors(nubmer)
        #
        Print(f'The factors of {nubmer}are{factors}')
except ValusError
    
    Print('That is an invalid number. Please input a positive interger.')