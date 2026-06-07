COLOR_MAP = {
    'black': '0',
    'brown': '1',
    'red': '2',
    'orange': '3',
    'yellow': '4',
    'green': '5',
    'blue': '6',
    'violet': '7',
    'grey': '8',
    'white': '9'
}

def label(colors):
    result_str = ""
    for i in range(2):
        result_str += COLOR_MAP[colors[i]]
    for i in range(int(COLOR_MAP[colors[2]])):
        result_str += '0'

    result_int = int(result_str)
    unit = 'ohms'
    if result_int // 1_000_000_000 > 0:
        unit = 'giga' + unit 
        result_int = result_int // 1_000_000_000
    elif result_int // 1_000_000 > 0:
        unit = "mega" + unit
        result_int =  result_int // 1_000_000
    elif result_int // 1_000:
        unit = 'kilo' + unit
        result_int = result_int // 1_000
    
    return f"{result_int} {unit}"
