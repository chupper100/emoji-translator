# The file test.py is used for testing perpose.
emoji = {
    "a": "ποΈ",
    "b": "ποΈ",
    "c": "ποΈ",
    "d": "π€£οΈ",
    "e": "ποΈ",
    "f": "ποΈ",
    "g": "ποΈ",
    "h": "ποΈ",
    "i": "ποΈ",
    "j": "ποΈ",
    "k": "ποΈ",
    "l": "ποΈ",
    "m": "ποΈ",
    "n": "ποΈ",
    "o": "ποΈ",
    "p": "βΊοΈ",
    "q": "ποΈ",
    "r": "π€οΈ",
    "s": "π€©οΈ",
    "t": "π€οΈ",
    "u": "π€¨οΈ",
    "v": "ποΈ",
    "w": "ποΈ",
    "x": "πΆοΈ",
    "y": "ποΈ",
    "z": "ποΈ",
}


def text_emoji(emoji):  # Text To Emoji
    input_text = str(input("Input: ")).lower()
    table = str.maketrans(emoji)
    output_text = input_text.translate(table)
    return output_text


def emoji_text(emoji):  # Emoji To Text
    input_text = input("Input: ")
    emoji_to_letter = {v.strip("\ufe0f"): k for k, v in emoji.items()}  # reserve
    table = str.maketrans(emoji_to_letter)
    output_text = input_text.translate(table)
    return output_text


def main(emoji):
    cases = {"t": emoji_text, "e": text_emoji}
    choice = input("What do you want to translate to? ").lower()
    func = cases.get(choice, "Please choose a valid option!")
    return func(emoji)


print(main(emoji))
