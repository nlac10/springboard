# NEW LESSON LEARNED:
# * isalnum() means alphabet & numbers. BUT these numbers are written as STRINGS

def LongestWord(sen):

  # code goes here
  longest_word = ""
  longest_len = 0


  words = [word for word in sen.lower().strip().split() if word.isalnum()]

  for word in words:
    if len(word) > longest_len:
      longest_len = len(word)
      longest_word = word
    elif len(word) == longest_len:
      longest_word = longest_word

  return longest_word

# keep this function call here
print(LongestWord(input()))


# >>> input
#   * string
#     - if two words are the same:
#       return the first word
#     # notes:
#     - clean: capitalization, spaces, punctuation, numbers
#     - not empty
#     - Q: are hypenated words count as one-word?

# >>> output
#   * string
#     - name of the longest word

# constraints
#   * ignore punctuation
#   * no string entered is empty
#   * if two+ words are the same, return first word

# flow
#   * def function
#   * clean: remove punc, space, numbers, lower it
#   * make into a list via split()
#   * for each word in the list, find the length
#   * have container holding the lenth of word
#   * if length of word compared to the baseline is greater, replace that length
#   * return the word (not length )
#   * no need to change list back to all strings
#   * use indexing to pull out and return needed word
