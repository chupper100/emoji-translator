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
output_text=''
input_text=str(input('Input:'))
for letter in input_text:
    if emoji.values[letter]:
        output_text=output_text+emoji.keys(letter)
    else:
        output_text=output_text+letter

print(output_text)
