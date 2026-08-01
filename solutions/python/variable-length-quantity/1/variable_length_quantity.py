def encode_single(num):
    binary = f"{num:b}"
    length = len(binary)
    mod = length % 7
    if mod != 0:
        binary = '0' * (7 - mod) + binary
    count = len(binary) // 7

    encoded = []
    for i in range(count):
        high_bit = '1'
        if i == count - 1:
            high_bit = '0'

        encoded.append(int(high_bit + binary[i * 7 : i * 7 + 7], 2))
    return encoded

def encode(numbers):
    encoded = []
    for n in numbers:
        encoded.extend(encode_single(n))
    return encoded


def decode_single(bytes_):
    binary = ""
    for byte in bytes_:
        binary += byte[1:8]
    return int(binary, 2)
    

def decode(bytes_):
    segments = []
    current = []
    for byte in bytes_:
        binary = f"{byte:08b}"
        current.append(binary)

        if binary[0] == '0':
            segments.append(current)
            current = []

    if current != []:
        raise ValueError("incomplete sequence")

    results = []
    for segment in segments:
        results.append(decode_single(segment))
    return results
