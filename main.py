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

def choose_mode():
    user_choice=input('ETT: Emoji To Text, TTE: Text To Emoji ').lower()
    return user_choice

output_text=''
def text_emoji(): #Text To Emoji
    output_text=''
    input_text=str(input('Input:')).lower()
    for letter in input_text:
        if letter in emoji:
            output_text=output_text+emoji[letter]
            print(i, output_text)
            i=i+1
        else:
            output_text=output_text+letter

def emoji_text(): #Emoji To Text
    input_text=str(input('Input:')).lower()


def main():
    choice=choose_mode()
    if choice=='ett':
        print('You choosed to translate emoji to text.')
        emoji_text()

    elif choice=='tte':
        print('You choosed to translate text to emoji.')
        text_emoji()

main()
print(output_text)