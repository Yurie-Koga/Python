
# Here are code solutions for each of the drawings from the starry.py exercise
# Of course, you didn't have to write functions! But since we learned about functions now,
# we have used functions here to separate out each drawing to clean up the code. :)


# Drawing Example

def draw_x(n: int):
    """The example but commented"""
    
    for row in range(n):            # loops through as many rows as the user asked for
        for column in range(row+1): # loops through as many columns as current row number
            print('*', end='')      # prints a star for each column, avoiding newline
        print()                     # print the newline only when the whole row is done


# Drawing 1

def draw_1(n: int):
    """Nested loop + end='' version"""
    
    for row in range(n):

        for col in range(n - row - 1):
            print(' ', end='')

        for col in range(2 * row + 1):
            print('*', end='')
            
        print()


# Drawing 2

def draw_2(n: int):
    """Simple reversal of example code"""

    for row in range(n):
        for col in range(n - row):
            print('*', end='')
        print()


# Drawing 3

def draw_3(n: int):
    """Version that doubles middle row for even numbers"""

    # Top half + middle
    for row in range(n // 2):
        for col in range(row + 1):
            print('*', end='')
        print()

    # Bottom half
    for row in range(n // 2, n):
        for col in range(n - row):
            print('*', end='')
        print()

def draw_3_alt(n: int):
    """
    Version that rounds even numbers down to nearest odd
    N.B. It would be trivial to round up instead
    """ 

    n = n - (n + 1) % 2 # cut even number down to nearest odd
    for row in range(n):
        dist_from_half = (abs(n // 2 - row))
        cols = n - n // 2 - dist_from_half
        for col in range(cols):
            print('*', end='')
        print()


# Drawing 4

def draw_4(n: int):
    """Version that doubles middle row for even numbers"""

    # Top half +  middle
    for row in range(n // 2 + (n % 2)):
        cols = n - row * 2
        
        for col in range((n - cols) // 2):
            print(' ', end='')

        for col in range(cols):
            print('*', end='')
            
        print()

    # Bottom half
    for row in range(n // 2):
        cols = (row + 1) * 2 + (n % 2)
        
        for col in range((n - cols) // 2):
            print(' ', end='')

        for col in range(cols):
            print('*', end='')
            
        print()

def draw_4_alt(n: int):    
    """
    Version that rounds even numbers down to nearest odd
    N.B. It would be trivial to round up instead
    """
    
    n = n - (n + 1) % 2 # cut even number down to nearest odd
    for row in range(n):
        dist_from_half = (abs(n // 2 - row))
        cols = 1 + dist_from_half * 2

        for col in range((n - cols) // 2):
            print(' ', end='')
        
        for col in range(cols):
            print('*', end='')
            
        print()

# Drawing 5

def draw_5(n: int):
    """Version that doubles middle row for even numbers"""

    # Top half +  middle
    for row in range(n // 2 + (n % 2)):
        cols = (row) * 2 + (n % 2)
        
        for col in range((n - cols) // 2):
            print(' ', end='')

        for col in range(cols):
            print('*', end='')
            
        print()

    # Bottom half
    for row in range(n // 2):
        cols = n - (row + 1) * 2
        
        for col in range((n - cols) // 2):
            print(' ', end='')

        for col in range(cols):
            print('*', end='')
            
        print()

def draw_5_alt(n: int):    
    """
    Version that rounds even numbers down to nearest odd
    N.B. It would be trivial to round up instead
    """
    
    n = n - (n + 1) % 2 # cut even number down to nearest odd
    for row in range(n):
        dist_from_half = (abs(n // 2 - row))
        cols = n - dist_from_half * 2

        for col in range((n - cols) // 2):
            print(' ', end='')
        
        for col in range(cols):
            print('*', end='')
            
        print()
        

# Run chosen drawing

choice = input("Choose a number or 'q' to quit: ").strip().lower()
while choice != 'q':

    n = int(choice)
    if n < 1:
        print("Invalid input.")
    else:
        print()

        draw_x(n)
        print("----Drawing 1----")
        draw_1(n)
        print("----Drawing 2----")
        draw_2(n)
        print("----Drawing 3----")
        draw_3(n)
        print("---Alternative drawing 3 for even n----")
        draw_3_alt(n)
        print("----Drawing 4----")
        draw_4(n)
        print("---Alternative drawing 4 for even n----")
        draw_4_alt(n)
        print("----Drawing 5----")
        draw_5(n)
        print("---Alternative drawing 3 for even n----")
        draw_5_alt(n)

    print()
    choice = input("Choose a number or 'q' to quit: ").strip().lower()


