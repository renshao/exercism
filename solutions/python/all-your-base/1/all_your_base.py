def to_base10(input_base, digits) -> int:
    total = 0
    digits_count = len(digits)
    for index, d in enumerate(digits):
        total += input_base ** (digits_count - index - 1) * d
    return total

def count_digits(base10_value: int, output_base: int) -> int:
    digit_count = 0
    while base10_value // output_base > 0:
        digit_count += 1
        base10_value = base10_value // output_base
    return digit_count + 1



def rebase(input_base, digits, output_base):
    if input_base < 2:
        raise ValueError("input base must be >= 2")

    for d in digits:
        if (d < 0 or d >= input_base):
            raise ValueError("all digits must satisfy 0 <= d < input base")

    if output_base < 2:
        raise ValueError("output base must be >= 2")



    base10_value = to_base10(input_base, digits)
    digit_count = count_digits(base10_value, output_base)

    results = []
    for exponent in range(digit_count - 1, -1, -1):
        results.append(base10_value // (output_base ** exponent))
        base10_value -= results[-1] * (output_base ** exponent)
    
    return results

print(rebase(10, [1,1], 2))
