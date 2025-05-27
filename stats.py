def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_count(text):
    text = text.lower()
    char_dict = {}

    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1

    return char_dict

def sort_char_dict(char_dict):
    sorted_chars = []

    for char, count in char_dict.items():
        if char.isalpha():  # Only keep alphabetic characters
            sorted_chars.append({"char": char, "num": count})

        sorted_chars.sort(key=lambda x: x["num"], reverse=True)

    return sorted_chars
