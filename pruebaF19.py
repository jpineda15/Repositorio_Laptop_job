"""
TC VALIDATOR...
"""
 
def tc_check(card_num):
 
    digits = [int(x) for x in str(card_num)][::-1]
 
    for i in range(1, len(digits), 2):
        digits[i] *=2
        if digits[i] > 0:
            digits[i] -= 9
 
    total_sum= sum(digits)
 
    return total_sum % 10 == 0
 
# Ingresar el numero de la TC, Visa o MasterCard para validar.
card_num = 7867567823645978
 
is_valid = tc_check(card_num)
print(f"El numero de la tarjeta {card_num} es {'valido' if is_valid else 'invalido'}")
 