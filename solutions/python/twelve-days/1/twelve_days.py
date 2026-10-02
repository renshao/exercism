int_to_day = {
    1: ('a', 'first', 'Partridge in a Pear Tree'),
    2: ('two', 'second', 'Turtle Doves'),
    3: ('three', 'third', 'French Hens'),
    4: ('four', 'fourth', 'Calling Birds'),
    5: ('five', 'fifth', 'Gold Rings'),
    6: ('six', 'sixth', 'Geese-a-Laying'),
    7: ('seven', 'seventh', 'Swans-a-Swimming'),
    8: ('eight', 'eighth', 'Maids-a-Milking'),
    9: ('nine', 'ninth', 'Ladies Dancing'),
    10: ('ten', 'tenth', 'Lords-a-Leaping'),
    11: ('eleven', 'eleventh', 'Pipers Piping'),
    12: ('twelve', 'twelfth', 'Drummers Drumming')
}


def recite_verse(n):
    day = int_to_day[n]
    result = [f"On the {day[1]} day of Christmas my true love gave to me:"]
    if n == 1:
        result.append(f" {day[0]} {day[2]}.")
        return "".join(result)

    for i in range(n, 1, -1):
        gift = int_to_day[i]
        result.append(f" {gift[0]} {gift[2]},")
    first_day = int_to_day[1]
    result.append(f" and {first_day[0]} {first_day[2]}.")
    return "".join(result)


def recite(start_verse, end_verse):
    return [recite_verse(i) for i in range(start_verse, end_verse + 1)]
