def translate_word(text):
    if text[0] in "aeiou" or text.startswith("xr") or text.startswith("yt"):
        return f"{text}ay"
    
    qu_index = text.find('qu')
    if qu_index >= 0:
        # Check all chars before 'qu'
        all_consonants = True
        for i in range(qu_index):
            if text[i] in "aeiou":
                all_consonants = False
                break
        if all_consonants:
            return f"{text[qu_index + 2:]}{text[0:qu_index+2]}ay"
    
    y_index = text.find('y')
    if y_index >= 1:
        # Check all chars before 'y'
        all_consonants = True
        for i in range(y_index):
            if text[i] in "aeiou":
                all_consonants = False
                break
        if all_consonants:
            return f"{text[y_index:]}{text[0:y_index]}ay"
    
    i = 0
    while text[i] not in "aeiou":
        i += 1
    if i > 0:
        return f"{text[i:]}{text[0:i]}ay"

    return text

def translate(text):
    words = text.split(' ')
    results = []
    for word in words:
        results.append(translate_word(word))
    return " ".join(results)
