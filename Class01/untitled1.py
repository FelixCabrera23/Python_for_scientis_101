def quadratic(a:float, b:float, c:float, x:float) -> float:   
    quadratic_term = a * (x ** 2)
    linear_term = b * x
    constant_term = c
    return quadratic_term + linear_term + constant_term

def f():
    """
    This takes b and returns b * 2
    NOTE : this func will change the x global
    >>> x = 1
    >>> x
    1
    >>> f(2)
    4
    >>> x
    4
    """
    
    global x
    x = b
    x *= 2
    return x

def days_difference(day1, day2):
    """
    Return the number of days between day1 and day2.
    The two days are assumed to be in
    the range 1-365, that is they
    indicate a day of the year.
    Examples:
    Examples:
    >>> days_difference(200, 224)
    24
    >>> days_difference(47, 47)
    0
    >>> days_difference(100, 99)
    -1
    """
    return day2 - day1

def conv_F_to_C(F:float)->float:
    """
    Returns the convertion from Farenheit to Celsius degrees
    
    F is the temperature in Farenheit
    
    C is the result temperature in Celsius
    
    >>> conv_F_to_C(90)
    32.22222222222222
    >>> conv_F_to_C(25)
    -3.8888888888888893
    """
    C = (F-32)*(5/9)
    return C

def Ex6 (a,b,c):
    return((a+b+c)/3)

def Ex7 (a,b,c,d):
    av1 = Ex6(b,c,d)
    av2 = Ex6(a,c,d)
    av3 = Ex6(a,b,d)
    av4 = Ex6(a,b,c)
    return(max(av1,av2,av3,av4))

