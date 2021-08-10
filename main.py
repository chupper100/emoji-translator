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

def text_emoji(): #Text To Emoji
    output_text=''
    input_text=str(input('Input:')).lower()
    for letter in input_text:
        if letter in emoji:
            output_text=output_text+emoji[letter]
        else:
            output_text=output_text+letter
    return output_text

def emoji_text(emoji): #Emoji To Text
    output_text=''
    emoji_to_letter = {v.strip('\ufe0f'): k for k, v in emoji.items()}
    table = str.maketrans(emoji_to_letter)

    input_text = input()
    output_text = input_text.translate(table)
    return output_text

def main(emoji):
    choice=input('ETT: Emoji To Text, TTE: Text To Emoji ').lower()
    if choice=='ett' or choice=='emoji to text':
        print('You have choosed to translate emoji to text.')
        print(emoji_text(emoji))
    elif choice=='tte' or choice=='text to emoji':
        print('You have choosed to translate text to emoji.')
        print(text_emoji())
    else:
        print('Please choose a valid option!')
        main()

main(emoji)
