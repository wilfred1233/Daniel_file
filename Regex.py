# 1- REGULAR EXPRESSION
# 2- INTRODUCTION TO REGEX
# 3- SIMPLE CHARACTERS MATCHES
# 4- CHARACTER CLASSES
# 5- SPECIAL CHARACTERS
# 6- QUANTIFIERS
# 7- SUBSTITUTION
# 8- COMPILING REGULAR EXPRESSION
# SPLIT FUNCTION


# COREY SCHAFER check him out!!!!!!!!!!!!!

import re
# 2

text = "cat bat mat rat"
pattern = "dart"

# re.findall(pattern, text)

output = re.findall(pattern, text)
print(output)


text_1 = 'cat bat mat cat rat'
output_1 = re.findall(pattern, text_1)
print(output_1)

my_text = 'The dog barks loudly'
pattern = 'dog'
print(re.findall(pattern, my_text))

# 3- CHARACTER CLASSES

text1 = 'abc 123 '
pattern = "\d"  # slash gives all the numbers found in the string
print(re.findall(pattern, text1))


text2 = 'abc def ghi jkl '
pattern = r'def'  # for extracting the string put outputting it individually
print(re.findall(pattern, text2))

text3 = 'Hello World! ab DEF 123'
pattern = r'[a-z]' # for extracting lowercase letters
print(re.findall(pattern, text3))

text3 = 'Hello World! ab DEF 123'
pattern = r'[A-Z]'  # for extracting uppercase letters
print(re.findall(pattern, text3))

text4 = 'abc def ghi jkl'
pattern= r'[^def]'
print(re.findall(pattern,text4))


text6 = 'Hello World 1234'
pattern = r'[a-zA-z]' # extracting for lower case and uppercase
print(re.findall(pattern, text6))

text = 'Hello World 1234 ^&**%$'
pattern = r'[a-zA-z0-9]'
print(re.findall(pattern, text))

text = 'Hello World 1234 ^&**%$'
pattern = r'[^a-zA-z0-9^\s]'  # trying not to extract numbers uppercase and lowercase
print(re.findall(pattern, text))

text = 'Hello World 1234 ^&**%$'
pattern = r'\s'  # trying not to extract spaces
print(re.findall(pattern, text))

text = 'Hello World 1234 &**%$'
pattern = r'[^a-fA-F0-9^\s]'  # trying  to extract symbols
print(re.findall(pattern, text))


# text= 'usernam023 AA$$'

# 4- SPECIAL CHARACTERS
text = 'hello world '
pattern = r'h.llo'
print(re.findall(pattern, text))


text= 'dello world hallo heeello'
pattern = r'h.*llo'
print(re.findall(pattern, text))


text = 'dello world falld heeello'
patten = '.ld'
print(re.findall(pattern, text))

text = 'dello world falld heeello'
pattern = '.*ld'
print(re.findall(pattern, text))

# 5-  QUANTIFIERS
text = 'a aa aaa aaaa aaaaa'
pattern = r'a*'  # extract for matches of 0 and more
print(re.findall(pattern, text))

pattern = r'a+'  # extract for matches of 1 and more
print(re.findall(pattern, text))

pattern = r'a{2}'  # pull out for matches of 2 occurences
print(re.findall(pattern, text))

pattern = r'a{2,}'  # pull out for matches of 2 occurences
print(re.findall(pattern, text))


pattern = r'a{3}'  # pull out for matches of 3 occurences
print(re.findall(pattern, text))

pattern = r'a{3,}'  # extract for matches of 3 occurence
print(re.findall(pattern, text))


pattern = r'a{4}'  # extract for matches of 4 and more
print(re.findall(pattern, text))

print('\\\\\\\\\\\\\\')
pattern = r'a{2,4}'  # pull out between 2 and 4 occurences
print(re.findall(pattern, text))
print('\\\\\\\\\\\\\\')

# 6- SUBSTITUTIONS
text =  'Daniel and Marvelous are friends'
pattern = 'friends'  # Word, we are trying to substitute
output = re.sub(pattern,'opps',text)
print(output)
# re.findall

# 7- COMPILING REGULAR EXPRESSION

text = 'There are 10 apples and 20 oranges'
pattern = '[0-9]'
print(re.findall(pattern, text))

text = 'There are 10 apples and 20 oranges'
pattern = '\d'
print(re.findall(pattern, text))

text = 'There are 10 apples and 20 oranges'
pattern = '\d+'
print(re.findall(pattern, text))

pattern = re.compile('\d+')
daniel_text = 'There are 10 apples, 30 mangoes and 20 oranges'
output = pattern.findall(daniel_text)
print(output)

# recap/random explanation

text = 'There are 10 apples and 20 oranges'
pattern = '[a-zA-Z]'
print(re.findall(pattern, text))

text = 'There are 10 apples and 20 oranges'
pattern = '[a-zA-Z]+'
print(re.findall(pattern, text))


# NOTE: \w == A-Za-z0-9
text = 'There are 10 apples and 20 oranges'
pattern = '[\w]+'  # to extract letters and numbers
print(re.findall(pattern, text))

# 8- SPLIT FUNCTION


text = 'Spilt this text for me right away'
pattern = r'\s+'  # split with respect to whitespaces
output = re.split(pattern, text)
print(output)
# print(text.split())
# print(text.split(' '))
# print(text.split('t'))

