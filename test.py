emoji={
    'a':'😀️',
    'b':'😁️',
    'c':'😂️',
    'd':'🤣️',
    'e':'😃️',
    'f':'😅️',
    'g':'😆️',
    'h':'😉️',
    'i':'😊️',
    'j':'😋️',
    'k':'😎️',
    'l':'😍️',
    'm':'😘️',
    'n':'😗️',
    'o':'😚️',
    'p':'☺️',
    'q':'🙂️',
    'r':'🤗️',
    's':'🤩️',
    't':'🤔️',
    'u':'🤨️',
    'v':'😐️',
    'w':'😑️',
    'x':'😶️',
    'y':'🙄️',
    'z':'😏️',
}

emoji_to_letter = {v.strip('\ufe0f'): k for k, v in emoji.items()}
table = str.maketrans(emoji_to_letter)

input_text = input()
output_text = input_text.translate(table)
print(output_text)
