def encode_message(message, key):
    cypher_text = ""
    i = 0

    for char in message:
        ascii_code = ord(char)
        number = ascii_code - ord('a')
        key_char = key[i % len(key)]
        ascii_char_code = ord(key_char)
        char_number = ascii_char_code - ord('a')
        number = (number + char_number) % 26
        number += ord('a')
        number = chr(number)
        i = i + 1
        cypher_text += number

    return cypher_text


print encode_message('huntthemdown', 'lunar') # wcsespsbnuhiedj
