VALID_OPERATORS = {'plus', 'minus', 'divided_by', 'multiplied_by'}

def is_number(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def validate_operator(operator):
    if operator not in VALID_OPERATORS:
        raise ValueError('unknown operation')

def apply_operator(op, a, b):
    match op:
        case 'plus':
            return a + b
        case 'minus':
            return a - b
        case 'multiplied_by':
            return a * b
        case 'divided_by':
            return a // b    


def answer(question):
    question = (question.replace('What is', '')
                        .replace('divided by', 'divided_by')
                        .replace('multiplied by', 'multiplied_by')
                        .replace('?', '')).strip()
    
    if question == '':
        raise ValueError('syntax error')

    stack = []

    for token in question.split(' '):
        if is_number(token):
            if not stack:
                stack.append(int(token))
            elif type(stack[-1]) is int:
                raise ValueError("syntax error")
            else:
                operator = stack.pop()
                total = stack.pop()
                stack.append(apply_operator(operator, total, int(token)))
        else:
            validate_operator(token)
            if not stack or type(stack[-1]) is str:
                raise ValueError("syntax error")
            else:
                stack.append(token)
    
    if type(stack[-1]) is not int:
        raise ValueError("syntax error")
    
    return stack[-1]
