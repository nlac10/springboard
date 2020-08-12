# NEW LESSON LEARNED:
"""
.iscapitalize() makes upp the FIRST character of the word only ('H3llo') whereas
.istitle() makes upper each word of the FIRST character ONLY IF ITS A LETTER of each ('H3Llo')
"""


def LetterCapitalize(str):

  text = [word.capitalize() for word in str.lower().strip().split()]

  return " ".join(text)

# keep this function call here
print(LetterCapitalize(input()))

# >>>input
# - string
# >>>output
# - string with first letter of word uppercase

# constraints:
# - what if input has different cases?
# - .title() only works with letters not numbers
# - separated by only ONE space

# flow:
#   def function
#   clean: lower, strip,split
#   list comp
#   try: upper the first letter via index
#     or word.title()
#   return
