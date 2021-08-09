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

def emoji_text(): #Emoji To Text
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
        if letter == emoji.values():
            print(emoji.keys(letter))
            #output_text=output_text+dic_letter
        else:
            pass#output_text=output_text+letter
    return output_text

def main():
    choice=input('ETT: Emoji To Text, TTE: Text To Emoji ').lower()
    if choice=='ett' or choice=='emoji to text':
        print('You have choosed to translate emoji to text.')
        print(emoji_text())
    elif choice=='tte' or choice=='text to emoji':
        print('You have choosed to translate text to emoji.')
        print(text_emoji())
    else:
        print('Please choose a valid option!')
        main()

main()