import string as s

def LetterChanges(str):

  modified_string = ""
  code = s.ascii_lowercase + "a"
  vowels = 'aeiou'

  # change code based on algorithm
  for char in str.lower().strip():

    if char in code:
      index = code.find(char)
      modified_string += code[index+1]

    elif char not in code:
      modified_string += char

  for character in modified_string:
    if character in vowels:
      modified_string = modified_string.replace(character, character.upper())




  return modified_string

# keep this function call here
print(LetterChanges(input()))


# >>> input
# * string
# - clean: lower (yes, but next you should ask if uppser should stay upper ),
# - strip white spaces
# - keep: punctuation, numbers (string)
# >>> ouput
# * string
# - same but ciphered
# - a == b, z == a, etc.
# - keep: spaces, punctuation, numbers
# - make vowels upper case

# constraints/assumptions:
# - keep spaces, punctuation, numbers (as strings)
# - make vowels upper regardless of position
# - everything is in lowercase
# - if punctuation or number, don't change it!

# flow:
# - define function
# - import string module?
# - define letter-changes, ascii-lowercase, add 'a' to it
# - clean: lower and strip
# - have empty holder for ans:
# - iterate through inputted string
# - for each letter, .find() in 'letter changes'
# - will return index
# - do index + 1
# - add this index + 1 in ans

# # for punc and numbers
# - if the char is NOT an alphabet, keep it the same
# - just add it to the final answer

# # for vowels
# - define vowels (lowercase)
# - iterate through modified string
# - if letter in 'vowels' string, uppercase it
# - return modified string
