import math

def display_welcome_menu():
    '''
    function that displays options to user 
    (none)-->none
    
    >>>display_welcome_menu()
    Welcome to the COMP 202 fair pizza calculator!
    Please chose one of the following modes:
    A. Quantity mode
    B. Price mode
    
    '''
    print("Welcome to the COMP 202 fair pizza calculator!")
    print("Please chose one of the following modes:")
    print('A. "Quantity mode"')
    print('B. "Price mode"')


# to use for get_fair_quantity()
def area(d):
    '''
    function that finds area of any given diameter 'd'
    (int)-->num
    
    >>>area(7)
    38.48451001
    >>>area(3)
    7.068583471
    >>>area(5)
    19.63495408
    >>>area(0)
    0
    
    '''
    r = d/2
    return(math.pi*(r**2))

def get_fair_quantity(x,y):
    '''
    function that always divides area of circle w largest diameter by smaller
    (int)-->int
    
    >>>print(get_fair_quantity(13,12))
    2
    >>>print(get_fair_quantity(12,13))
    2
    >>>print(get_fair_quantity(10,10))
    1
    >>>print(get_fair_quantity(10,0))
    ZeroDivisionError
    >>>print(get_fair_quantity(5,10))
    4

    '''
# Order of entry should not matter,
# if/else statement means greater value will always be divided by smaller
    if(x>=y):
        fair_quantity=math.ceil(area(x)/area(y))
    else:
        fair_quantity=math.ceil(area(y)/area(x))
    return fair_quantity


def get_fair_price(diameter_large,price_large,diameter_small,quantity_small):
    '''
    function that calculates the fair price to pay for no. of small pizzas
    compared to price of large pizza
    (int,float,int,int)-->float
    
    >>>print(get_fair_price(3,10.55,3,1))
    10.55
    >>>print(get_fair_price(8,5.333345,5,2))
    4.17
    >>>print((get_fair_price(3,2.0,1,1))
    0.22
    >>>print(get_fair_price(5,0,3,6))
    ZeroDivisionError
    
    '''

# variable that finds the price of large pizza per dollar
    pizza_per_dollar=float((area(diameter_large)/price_large))

# variable that finds total area of all small pizzas desired
    total_area_small=float(area(diameter_small)*quantity_small)

# variable that calculates the fair price to pay for no. of small pizzas
#  compared to price of large pizza
    fair_price=round((total_area_small/pizza_per_dollar),2)
    return(fair_price)


def run_pizza_calculator():
    '''
    function that runs pizza calculator
    displays menu, takes user's input and tells user either:
    how many small pizzas=1 large pizza or
    how much a value of small pizzas should cost,
    if at the same pizza/$ as large pizza

    (none)-->none
    
    >>>run_pizza_calculator()
    Welcome to the COMP 202 fair pizza calculator!
    Please chose one of the following modes:
    A. Quantity mode
    B. Price mode
    Enter your choice:.
    Enter the diameter of the large pizza:
    Enter the diameter of the small pizza:
    To be fully satisfied you should order 2 small pizzas
    
    >>>run_pizza_calculator()
    Welcome to the COMP 202 fair pizza calculator!
    Please chose one of the following modes:
    A. Quantity mode
    B. Price mode
    Enter your choice:B
    Enter the diameter of the large pizza:17
    Enter the price of the large pizza:13.3334
    Enter the diameter of the small pizza:15
    Enter the number of small pizzas you'd like to buy:6
    "The fair price to pay for 1 small pizzas is $62.28
    
    >>>run_pizza_calculator()
    Welcome to the COMP 202 fair pizza calculator!
    Please chose one of the following modes:
    A. Quantity mode
    B. Price mode
    Enter your choice:b
    This mode is not supported
    
    >>>run_pizza_calculator()
    Welcome to the COMP 202 fair pizza calculator!
    Please chose one of the following modes:
    A. Quantity mode
    B. Price mode
    Enter your choice:3
    This mode is not supported
    
    >>>run_pizza_calculator()
    Welcome to the COMP 202 fair pizza calculator!
    Please chose one of the following modes:
    A. Quantity mode
    B. Price mode
    Enter your choice:!
    This mode is not supported
    
    
    '''
    display_welcome_menu()
    
    menu_choice=input("Enter your choice: ")
    
    if (menu_choice=='A'):
        print( 'You selected "Fair Quantity" mode' )
        Diameter_Large =int(input("Enter the diameter of the large pizza: "))
        Diameter_Small=int(input("Enter the diameter of the small pizza: "))
        
        print("To be fully satisfied you should order " + str(get_fair_quantity(Diameter_Large,Diameter_Small)) + " small pizzas")
        
        
    elif (menu_choice=='B'):
        print( 'You selected "Price mode"' )
        Diam_Large= int(input("Enter the diameter of the large pizza: "))
        Price_Large= float(input("Enter the price of the large pizza: "))
        Diam_Small= int(input("Enter the diameter of the small pizza: "))
        No_Pizzas= int(input("Enter the number of small pizzas you'd like to buy: "))

#variable that returns the function get_fair_price, to display as string in
# final message
        fair_price_result= get_fair_price(Diam_Large,Price_Large,Diam_Small,No_Pizzas)
        
        print("The fair price to pay for " + str(No_Pizzas) + " small pizzas is $" + str(fair_price_result))
    
    else:
        print("This mode is not supported")
        
    






