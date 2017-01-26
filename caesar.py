def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in letter:
        pos = alphabet.index(char)
        if pos < 26:
            pos= pos
        else:
            pos= pos-26
        return pos

def rotate_character(char,rot):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char in alphabet:
        pos = alphabet.index(char)
        if pos < 26:
            letter = pos + rot
            if letter < 52:
                rot = alphabet[letter]
                rot = rot.lower()
            else:
                letter = letter % 26
                rot = alphabet[letter]
                rot = rot.lower()

        elif pos >= 26:
            letter = pos + rot
            if letter < 52:
                rot = alphabet[letter]
                rot = rot.upper()
            else:
                letter = letter % 26
                rot = alphabet[letter]
                rot = rot.upper()
        return rot
    else:
        return char

def encrypt(text, rot):
    new = text
    new = list(new)
    x = ""
    for value in new:
        new_elem = rotate_character(value, rot)
        x = x + new_elem
    return x
