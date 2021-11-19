emoji = {
    "a": "😀️",
    "b": "😁️",
    "c": "😂️",
    "d": "🤣️",
    "e": "😃️",
    "f": "😅️",
    "g": "😆️",
    "h": "😉️",
    "i": "😊️",
    "j": "😋️",
    "k": "😎️",
    "l": "😍️",
    "m": "😘️",
    "n": "😗️",
    "o": "😚️",
    "p": "☺️",
    "q": "🙂️",
    "r": "🤗️",
    "s": "🤩️",
    "t": "🤔️",
    "u": "🤨️",
    "v": "😐️",
    "w": "😑️",
    "x": "😶️",
    "y": "🙄️",
    "z": "😏️",
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
