import string
def word_analyzer():
  print('Welcome to my Word Analyzer!')
  print(' ')
  print('''
In this word analyzer, it will tell you how much of your text has lowercase and uppercase letters, the percentage of text that has lowercase and uppercase letters, spaces in the text, punctuation in the text, numbers in the text and more that I can\'t fit in here!
''')
  print(' ')
  print('\nThey can fit here! It can also show the percentage of numbers, spaces')
  print('''
and punctuation in the text.
''')
  message = input('Type In here to start the analyzer!: ')
  spaces = 0
  uppercase_letters = 0
  undercase_letters = 0
  punctuation = 0
  digits = 0
  for letter in message:
    if letter.isdigit():
      digits += 1
      continue

    if letter.isspace():
      spaces += 1
      continue

    if letter.islower():
      undercase_letters += 1
      continue

    if letter in string.punctuation:
      punctuation += 1
      continue

    if letter.isupper():
      continue

    uppercase_letters += 1

  total = len(message)
  full_total = uppercase_letters+undercase_letters+digits+punctuation+spaces
  if full_total == total:
    print('''
Everything is running correctly!
''')
  else:
    print('\nThe result is not correct!')

  percentage_of_lowercase = round(undercase_letters/total*100)
  percentage_of_uppercase = round(uppercase_letters/total*100)
  percentage_of_digits = round(digits/total*100)
  percentage_of_spaces = round(spaces/total*100)
  percentage_of_punctuation = round(punctuation/total*100)
  print('After some careful reading, your message has:')
  print(f'''- {digits} {pluralize(digits,'number')}''')
  print(f'''- {undercase_letters} {pluralize(undercase_letters,'letter')}''')
  print(f'''- {punctuation} {pluralize(punctuation,'punctuation mark')}''')
  print(f'''- {uppercase_letters} {pluralize(uppercase_letters,'letter')}''')
  print(f'''- {spaces} {pluralize(spaces,'space')}''')
  print('''
               -------Percentages-------         
''')
  print(f'''Lowercase Letters: {percentage_of_lowercase}% of your message were lowercase letters.''')
  print(f'''\nUppercase Letters: {percentage_of_uppercase}% of your message were uppercase letters.''')
  print(f'''\nNumbers: {percentage_of_digits}% of your message had {digits} {pluralize(digits,'number')}.''')
  print(f'''\nPunctuation: {percentage_of_punctuation}% of your message had punctuation.''')
  print(f'''\nSpaces: {percentage_of_spaces}% of your message had {spaces} {pluralize(spaces,'space')}.''')
  input('\nPress Enter to exit...')

def pluralize(count,word):
  if count == 1:
    return word
  else:
    return word+'s'

if __name__ == '__main__':
  word_analyzer()
