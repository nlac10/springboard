def KUniqueCharacters(str):

  ### k = number of unique chars in substring
  k = int(str[0])

  ### strip k from the main string
  str = str[1:]

  temp_str = ""
  max_temp_str = ""

  ### ALGORITHM
  ### for i from [0:len(str)]
  ###   1) create temp_str until we hit k unique characters
  ###   2) is temp_str > max_temp_str? update if yes

  for i in range(0,len(str)) :

#    str2 = str[i:]
#    for j in range(0,len(str2)):
#      temp_str += str2[j]

    for j in range(0,len(str[i:])):
      temp_str += str[i+j]
      # print(temp_str)
#
      ### if the current temp string has more unique chars than k
      ###    a) get rid of the last character appended
      ###    b) break inner (j) loop
      if(len(set(temp_str)) > k):
        temp_str = temp_str[:-1]
        break

    ### update with newest max if found
    if(len(temp_str) > len(max_temp_str) ):
      max_temp_str = temp_str

    ### reset temp_str
    temp_str = ""
    # print("\n\nRESET\n\n")

  str = max_temp_str

  # code goes here
  return str

# keep this function call here
print(KUniqueCharacters(input()))
