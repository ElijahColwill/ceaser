def encode_character(character, key):
    ascii_code = ord(character)
    number = ascii_code - ord('a')
    number = (number - key) % 26
    number += ord('a')
    return chr(number)

def encode(message, key):
    cypher_text = ""

    for char in message:
        cypher_text += encode_character(char, key)

    return cypher_text

print encode('dbu', 1) # cat
print encode('dssoh', 3) # apple
