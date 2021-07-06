"""v1.1
Identification card number checker （身份证号码检验）

This small program has only one aim - to test whether or not the national
ID card number is valid. No data will be transferred!"""

def create_weight_list():
    """Return a list containing the weight for each digit of ID card number."""
    
    result = []
    weight = 0
    for i in range(1, 18):
        weight = (2 ** (18 - i)) - ((2 ** (18 - i)) // 11) * 11
        result.append(weight)
    return result

def calculate_verification_number(id_without_ver: str) -> str:
    """Return the verification number for a given ID card number's first 17
    digits, i.e. id_without_ver.
    
    Precondition: len(id_without_ver) == 17
    
    >>> calculate_verification_number('35012119120623121')
    '0'
    """
    
    lst = create_weight_list()
    total_sum = 0
    result = 0
    
    for i in range(0, 17):
        total_sum += lst[i] * int(id_without_ver[i])
    
    temp = 12 - (total_sum - (total_sum // 11) * 11)
    result = str(temp - (temp // 11) * 11)
    
    if result == '10':
        result = 'X'

    return result


# Main

prompt = 'Enter your ID card number here (type return to continue): '
id_card = input(prompt)

while id_card == '' or len(id_card) <= 17:
    print('The ID you have entered is not valid. Please try again.')
    id_card = input(prompt)
    
while id_card != '':
    id_without_ver = id_card[:-1]
    verification_number = str(calculate_verification_number(id_without_ver))
    final_id = id_without_ver + verification_number  
    
    if id_card == final_id:
        print('The ID you have entered is valid.')
        break

    else:
        print('The ID you have entered is not valid. Please try again.')
        id_card = input(prompt)
        break
