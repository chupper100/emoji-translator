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

def text_emoji(emoji): #Text To Emoji
    input_text=str(input('Input:')).lower()
    table = str.maketrans(emoji)

    output_text = input_text.translate(table)
    return output_text

def emoji_text(emoji): #Emoji To Text
    input_text = input()
    emoji_to_letter = {v.strip('\ufe0f'): k for k, v in emoji.items()} #reserve
    table = str.maketrans(emoji_to_letter)

    output_text = input_text.translate(table)
    return output_text

def main(emoji):
    choice=input('What do you want to translate to? ').lower()
    if choice=='text' or choice=='t':
        print('You have choosed to translate emoji to text.')
        print(emoji_text(emoji))
    elif choice=='emoji' or choice=='e':
        print('You have choosed to translate text to emoji.')
        print(text_emoji(emoji))
    else:
        print('Please choose a valid option!')
        main(emoji)

main(emoji)
