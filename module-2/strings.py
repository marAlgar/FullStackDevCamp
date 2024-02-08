# sentence = 'The quick brown fox jumped'
# sentence -> variable 
# 'The quick brown fox jumped' -> string
# = -> assignment

""" sentence = 'The quick brown fox jumped'
sentence_two = sentence.upper()

print(sentence)
print(sentence_two) """

# .upper() -> turns into uppercase
# can be placed after the string or after the variable
# sentence = 'The quick brown fox jumped'.upper() == sentence.upper()


# The quick brown fox jumped
# T => 0 h => 1 e => 2...

""" starter_sentence = 'The quick brown fox jumped'
new_sentence = 'Thy' + starter_sentence[3:]

print(new_sentence) """


# Heredocs, multiline strings

content = """
Nullam id dolor id nibh ultricies vehicula ut id elit. Nullam quis risus eget urna mollis ornare vel eu leo.

Vestibulum id ligula porta felis euismod semper. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Cras justo odio, dapibus ac facilisis in.

Integer posuere erat a ante venenatis dapibus posuere velit aliquet.
""".strip() # removes the leading and trailing whitespaces

print(repr(content)) # repr() -> representation of the string

