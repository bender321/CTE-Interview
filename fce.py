def is_even(number):

    odd_digits = {'1', '3', '5', '7', '9'}
    odd_cases = {

        'one', 'three', 'five', 'seven', 'nine',
        'eleven', 'thirteen', 'fifteen', 'seventeen', 'nineteen'
    }
    even_cases = {

        'zero', 'two', 'four', 'six', 'eight', 'ten', 'twelve', 'fourteen', 'sixteen',
        'eighteen', 'twenty', 'thirty', 'fourty', 'fifty', 'sixty', 'seventy', 'eighty',
        'ninety', 'hundred', 'hundreds', 'thousand', 'thousands', 'milion', 'milions',
        'bilion', 'bilions', 'even'
    }

    formatted_number = (str(number)).lower()

    if formatted_number.isdigit():
        item = formatted_number
        if item[-1:] in odd_digits:
            return False
        else:
            return True
    else:
        formatted_number = formatted_number.replace('-', ',')
        formatted_number = formatted_number.replace(' ', ',')
        formatted_number = formatted_number.split(',')

        item = formatted_number[-1]

        if item in odd_cases:
            return False
        elif item in even_cases:
            return True






