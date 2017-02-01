from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    first = ""
    second = ""
    operator = ""
    data = {}
    if request.method == 'GET':
    	if request.GET.get('first_operator'):
    	    first = request.GET.get('first_operator')
    	if request.GET.get('second_operator'):
    	    second = request.GET.get('second_operator')
    	if request.GET.get('operator'):
    	    operator = request.GET.get('operator')
    	if first and second and operator:
    	    output = roman_arithematic_operation(first,second, operator)
    	    # data = {'output':output, 'first':first, 'second':second,'operator':operator}
    	    resultstring= first + operator + second+ "=" + output
    	    data = {"result":resultstring}
    return render(request, 'webapp/home.html', data)

numeral_map = tuple(zip(
    (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1),
    ('M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I')
))

def int_to_roman(i):
    try:
        if type(i) != type(1):
          #raise TypeError,"expected integer, got %s" % type(i)
            return "wrong type"
        if i >0 and i<4000:
            result = []
            for integer, numeral in numeral_map:
                count = i // integer
                result.append(numeral * count)
                i -= integer * count
            return ''.join(result)
        else:
            return 'operation should be possible only in the range of I to MMMCMXCIX'
    except:
        raise

def roman_to_int(n):
    i = result = 0
    for integer, numeral in numeral_map:
        while n[i:i + len(numeral)] == numeral:
            result += integer
            i += len(numeral)
    return result

def roman_arithematic_operation(first_roman_number, second_roman_number, operator):
    try:
        first_integer_number = roman_to_int(first_roman_number)
        second_integer_number = roman_to_int(second_roman_number)
        result = ""
        if first_integer_number is not None and second_integer_number is not None:
            if operator == "+":
                result = first_integer_number + second_integer_number
            elif operator == "-":
                result = first_integer_number - second_integer_number
            elif operator == "*":
                result = first_integer_number * second_integer_number
            elif operator == "/":
                result = first_integer_number / second_integer_number
            else:
                print("Enter a valid operator")
        else:
            return 'wrong input'
        
        return int_to_roman(result)
    except:
        raise
