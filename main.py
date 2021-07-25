
emoji={'a': '😀️',
 'b': '😁️',
  'c':'😂️',
   'd': '🤣️',
    'e',
     'f',
      'g',
       'h',
        'i',
         'j', 
         'k',
          'l',
           'm',
            'n',
             'o', 
             'p',
              'q',
               'r',
                's',
                 't',
                  'u',
                   'v',
                    'w',
                     'x',
                      'y',
                       'z'}
input_text=str(input('Input:')).lower()
print(input_text)
output_text=''
for word in input_text:
	if word in emoji:
		output_text=output_text+emoji[word]
	else:
		output_text=output_text+word
print(output_text)
