# -*- coding: utf-8 -*-
"""
Date Conversion
"""

#####
# Date string conversion: slash-date format to dash-date format
#####


def convert_day(day_string):
    """
    Converts day string from slash-date to dash-date format

    Assumes day between '1' or '01' and '31'

    Parameters:
    day_string: string containing day number in slash-date format

    Returns:
    string containing day number in dash-date format

    Example use:
    >>> convert_day('8')
    '08'
    >>> convert_day('15')
    '15'
    """
    # Your code here. Don't change anything above.
    if len(day_string) == 1:
        return str(0) + day_string
    else:
        return day_string
    
convert_day('8')
convert_day('15')

def convert_month(month_string):
    """
    Converts month string from slash-date to dash-date format

    Assumes month between '1' or '01' and '12'

    Parameters:
    month_string: string containing month number in slash-date format

    Returns:
    string containing month number in dash-date format

    Example use:
    >>> convert_month('3')
    '03'
    >>> convert_month('11')
    '11'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if len(month_string) == 1:
        return str(0) + month_string
    else:
        return month_string

convert_month('3')
convert_month('11')

def convert_year(year_string):
    """
    Converts year string from slash-date to dash-date format

    Assumes the year is either between '00' and '99' or between '1000' and '9999'
    
    If the year is between '00' and '99', assumes the year is in 1921-2020
    
    Parameters:
    year_string: string containing year number in slash-date format

    Returns:
    string containing year number in dash-date format

    Example use:
    >>> convert_year('03')
    '2003'
    >>> convert_year('25')
    '1925'
    >>> convert_year('1945')
    '1945'
    >>> convert_year('1389')
    '1389'
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    if len(year_string) == 2 and int(year_string) <= 20:
        return str(20) + year_string
    elif len(year_string) == 2 and int(year_string) > 20:
        return str(19) + year_string
    else:
        return year_string

convert_year('03')
convert_year('25')
convert_year('1945')
convert_year('1389')
convert_year('20')
convert_year('21')


def date_conversion(date_string):
    """
    Converts date string from slash format to dash format

    Assume European date ordering (day-month-year).
    Assume that two-digit years are in the past century (1921-2020 is "past century", 2021- is not...).
    Assume that the year of the date is in either range 00 - 99 or 1000 - 9999

    Parameters:
        date_string: string date in "slash" format, eg, 19/8/16, 1/12/1898, 1/1/25 (assume valid dates)

    Returns:
        string date in "dash" format, eg, 19-08-2016, 01-12-1898, 01-01-1925

    Example use:
    >>> print(date_conversion('19/8/16'))
    19-08-2016
    >>> print(date_conversion('01/12/1898'))
    01-12-1898
    >>> print(date_conversion('18/4/25'))
    18-04-1925
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW

    date_as_list = date_string.split('/')  # Use this to split slash format string into a list
    
    # Your code should call the three functions above to solve the problem. 
    # You will need to implement them first.
    date_as_list[0] = convert_day(date_as_list[0])
    date_as_list[1] = convert_month(date_as_list[1])
    date_as_list[2] =  convert_year(date_as_list[2])
    return str(date_as_list[0]) + '-' + str(date_as_list[1]) + '-' + str(date_as_list[2])


##### 
# Robust version of date conversion
#####


def date_conversion_robust(date_string):
    """
    Converts date string from slash format to dash format.
    Checks if input date is valid; if not, prints an error and returns None.

    Valid dates are as follows:
    - European date ordering (day-month-year).
    - Two-digit years are in the past century (1921-2020 is "past century", 2021- is not...).
    - The year of the date is in either range 00 - 99 or 1000 - 9999
    - An actual date that has occurred or will occur

    Parameters:
        date_string: string date in "slash" format, eg, 19/8/16, 1/12/1898, 1/1/25 (DO NOT assume every input is a valid date)

    Returns:
        if input was valid: return string date in "dash" format, eg, "19-08-2016", "01-12-1898", "01-01-1925"
        if input was not valid: print "Not a valid date." then return the default return value None

    Example use:
    >>> print(date_conversion_robust('19/8/16'))
    19-08-2016
    >>> print(date_conversion_robust('1/12/1898'))
    01-12-1898
    >>> print(date_conversion_robust('16/3/25'))
    16-03-1925
    >>> print(date_conversion_robust('29/2/2017'))
    Not a valid date.
    None
    >>> date_conversion_robust('131/2/1928')
    Not a valid date.
    >>> print(date_conversion_robust(2))
    Not a valid date.
    None
    """
    # DON'T CHANGE ANYTHING ABOVE
    # YOUR CODE BELOW
    can_split = ''
    date_as_list = []
    day_result = ''
    month_result = ''
    year_result = ''
    
    #date_as_list = date_string.split('/') 
    
    #day 
    try:
        date_as_list = date_string.split('/') 
        if len(date_as_list[0]) <= 2:
           
            #months with 31 days
            if int(date_as_list[1]) in [1,3,5,7,8,10,12]: #check that it is actual number of days for given month
                if int(date_as_list[0]) <= 31:
                    day_result = convert_day(date_as_list[0])
                else:
                    day_result = 'Not a valid date.'
            
            #months with 30 days
            elif int(date_as_list[1]) in [4,6,9,11]:
                if int(date_as_list[0]) <= 30:
                    day_result = convert_day(date_as_list[0])
                else:
                    day_result = 'Not a valid date.'
                
            #leap year       
            elif int(date_as_list[1]) == 2: #if month is february
                if int(date_as_list[2]) % 4 == 0:
                     if date_as_list[1] % 100 != 0: #
                         day_result = convert_day(date_as_list[0])
                     else:
                         if date_as_list[1] % 400 == 0: #this exactly devided by 400 is leap year
                             day_result = convert_day(date_as_list[0])
                         else:
                             day_result = 'Not a valid date.'
                else:
                    day_result = 'Not a valid date.'     
            else:
                day_result = 'Not a valid date.'     
        else:
            day_result =  'Not a valid date.'
        
        #month
        if len(date_as_list[1]) <= 2 and int(date_as_list[1]) <= 12 :
            month_result = convert_month(date_as_list[1])
        else: 
            month_result = 'Not a valid date.'
        
        #year
        if (len(date_as_list[2]) == 2 or len(date_as_list[2]) == 4):
            year_result = convert_year(date_as_list[2])
        else: 
            year_result = 'Not a valid date.'
    except:
        can_split = 'Not a valid date.'
        
    #check for leap year
    if day_result == 'Not a valid date.' or month_result == 'Not a valid date.' or year_result == 'Not a valid date' or can_split == 'Not a valid date.':
        correct_date = 'Not a valid date.'
        print('Not a valid date.')
        return None
    else:
        correct_date = day_result+ str('-') + month_result + str('-') + year_result
        return correct_date
    


def comparison_function(value):
    """
    Comparison function for counting_sort
    
    Parameter:
        value - integer
        
    Returns:
        ??? such that comparisons of return values work as described
    
    Example use:
    >>> comparison_function(99) > comparison_function(18783479)
    True
    >>> comparison_function(123) > comparison_function(321)
    False
    >>> comparison_function(1789) > comparison_function(96861)
    True
    """
    number_ninetozero = []
    for i in range(10)[::-1]:
        number_ninetozero.append(len([x for x in str(value) if x == str(i)]))
    number_ninetozero.append(int(value))
    return number_ninetozero


def counting_sort(items):
    """
    Sorts a list of integers by counting different digits.
    
    Parameters:
        items - list of positive integers
        
    Returns:
        sorted copy of items
        
    Example use:
    >>> counting_sort([98, 19, 29, 41, 9999, 73, 241, 1111, 53, 3, 333])
    [1111, 3, 333, 41, 241, 53, 73, 19, 29, 98, 9999]
    >>> counting_sort([999, 19, 919, 111, 119, 1199, 911])
    [111, 19, 119, 911, 919, 1199, 999]
    >>> counting_sort([1234, 4321, 3214, 2413])
    [1234, 2413, 3214, 4321]
    """
    # Please do NOT edit this function.
    return sorted(items, key=comparison_function)


