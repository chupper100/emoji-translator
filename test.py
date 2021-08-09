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

emoji_dict={k:v for v,k in emoji.items()}

print(emoji_dict)
input_text=str(input('Input:'))
output_text=''
for letter in input_text:
    if letter in emoji_dict:
        print(emoji_dict[letter])
        output_text=output_text+emoji_dict[letter]
    else:
        output_text=output_text+letter

print(output_text)
