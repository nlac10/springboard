"""
REMEMBER THIS ONE! your logic was wrong (see below) with specific case "+d+===+c+"
where it kept returning false when it should be true.

"""
import string as s

def SimpleSymbols(string):

  # clean
  text = string.lower().replace(" ","").strip()
  alphabet = s.ascii_lowercase

  # indexing
  # letters that start and end the string breaks the pattern
  if text[0].isalpha():
    return 'false'
  elif text[-1].isalpha():
    return 'false'

"""
Wrong Code:
  if not text[0].isalpha():
    return 'false'
elif not text[-1].isalpha():
    return 'false'
"""
  # use slicing with range
  for l in range(1,len(text)-1):
    if text[l] in alphabet:
      if not (text[l-1] == '+' and text[l+1] == '+'):
        return 'false'
  return 'true'


# def SimpleSymbols(str):
#
#     # code goes here
#   letters = 'abcdefghijklmnopqrstuvwxyz'
#   if len(str) < 3:
#     return 'false'
#
#   if (str[0] in letters) or (str[-1] in letters):
#     return 'false'
#
#   for i in range(1, len(str)-1):
#     if str[i] in letters:
#       if not (str[i-1] == '+' and str[i+1] == '+'):
#         return 'false'
#   return 'true'


# keep this function call here
# print(SimpleSymbols(input()))
