def is_valid(isbn):
    cleaned = isbn.replace('-', '')

    if len(cleaned) != 10:
        return False
    
    digits = []
    # Append first 9 digits
    for i in range(9):
        c = cleaned[i]
        if not c.isdigit():
            return False
        
        digits.append(int(c))
    # Append the 10th digit
    c = cleaned[9]
    if not (c.isdigit() or c.upper() == 'X'):
        return False
    if c.upper() == 'X':
        digits.append(10)
    else:
        digits.append(int(c))
    
    total = 0
    for i, digit in enumerate(digits):
        total += digit * (10 - i)
    
    return total % 11 == 0
