def dots_to_mask(*dots):
    mask = 0
    for d in dots:
        if 1 <= d <= 6:
            mask |= 1 << (d - 1)
    return mask

BRAILLE_MAP = {
    "A": dots_to_mask(1),
    "B": dots_to_mask(1, 2),
    "C": dots_to_mask(1, 4),
    "D": dots_to_mask(1, 4, 5),
    "E": dots_to_mask(1, 5),
    "F": dots_to_mask(1, 2, 4),
    "G": dots_to_mask(1, 2, 4, 5),
    "H": dots_to_mask(1, 2, 5),
    "I": dots_to_mask(2, 4),
    "J": dots_to_mask(2, 4, 5),
    "K": dots_to_mask(1, 3),
    "L": dots_to_mask(1, 2, 3),
    "M": dots_to_mask(1, 3, 4),
    "N": dots_to_mask(1, 3, 4, 5),
    "O": dots_to_mask(1, 3, 5),
    "P": dots_to_mask(1, 2, 3, 4),
    "Q": dots_to_mask(1, 2, 3, 4, 5),
    "R": dots_to_mask(1, 2, 3, 5),
    "S": dots_to_mask(2, 3, 4),
    "T": dots_to_mask(2, 3, 4, 5),
    "U": dots_to_mask(1, 3, 6),
    "V": dots_to_mask(1, 2, 3, 6),
    "W": dots_to_mask(2, 4, 5, 6),
    "X": dots_to_mask(1, 3, 4, 6),
    "Y": dots_to_mask(1, 3, 4, 5, 6),
    "Z": dots_to_mask(1, 3, 5, 6),

    "#": dots_to_mask(3,4,5,6),   # signe numérique
    "^": dots_to_mask(6),   # signe alpha
    
    "1": dots_to_mask(1),
    "2": dots_to_mask(1, 2),
    "3": dots_to_mask(1, 4),
    "4": dots_to_mask(1, 4, 5),
    "5": dots_to_mask(1, 5),
    "6": dots_to_mask(1, 2, 4),
    "7": dots_to_mask(1, 2, 4, 5),
    "8": dots_to_mask(1, 2, 5),
    "9": dots_to_mask(2, 4),
    "0": dots_to_mask(2, 4, 5),

    " ": 0
}

def normalize_char(ch):
    if not ch:
        return None

    ch = str(ch).strip().upper()

    if len(ch) == 0:
        return " "

    ch = ch[0]

    if ch in BRAILLE_MAP:
        return ch

    return None

def char_to_mask(ch):
    c = normalize_char(ch)
    if c is None:
        return None
    return BRAILLE_MAP[c]
