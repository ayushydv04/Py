#docstring ek function ke baare m bataati hai
# comment nhi h, comments ki trha ignore nhi kiya jaata, show krne ke liye print(function_name.__doc__)
def square(n):
    '''Prints the square of the number'''       # docstring ko right below the function hi print krna hai
    print(n**2)
square(5)
print (square.__doc__)      # docstring ko print krana


