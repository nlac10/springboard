"""
Project: Birds of Paradise
Description:

"""

# make dictionary
rarebirds = {'Gold-crested Toucan':
                { 'Height (m)':1.1,
                  'Weight (kg)':35,
                  'Color':'Gold',
                  'Endangered':True,
                  'Aggressive':True,},
            'Pearlescent Kingfisher':
                { 'Height (m)':0.25,
                  'Weight (kg)':0.5,
                  'Color':'White',
                  'Endangered':False,
                  'Aggressive':False,},
            'Four-metre Hummingbird':
                { 'Height (m)':0.6,
                  'Weight (kg)':0.5,
                  'Color':'Blue',
                  'Endangered':True,
                  'Aggressive':False,},
            'Giant Eagle':
                { 'Height (m)':1.5,
                  'Weight (kg)':52,
                  'Color':'Black and White',
                  'Endangered':True,
                  'Aggressive':True,},
            'Ancient Vulture':
                { 'Height (m)':2.1,
                  'Weight (kg)':70,
                  'Color':'Brown',
                  'Endangered':False,
                  'Aggressive':False,},
            }

# checks out!
# print(rarebirds)

## Create list of possible locations, code locations, and actions

birdlocation = ["In the canopy directly above our heads.",
"Between my 6 and 9 o’clock above.",
"Between my 9 and 12 o’clock above.",
"Between my 12 and 3 o’clock above.",
"Between my 3 and 6 o’clock above.",
"In a nest on the ground.",
"Right behind you."]

# check it out
# print(birdlocation[3])

# dict of binary code to communicate with photographer

codes = {111: "In the canopy directly above our heads.",
        110:"Between my 6 and 9 o’clock above.",
        101:"Between my 9 and 12 o’clock above.",
        100:"Between my 12 and 3 o’clock above.",
        "011":"Between my 3 and 6 o’clock above.",
        "010":"In a nest on the ground.",
        "001":"Right behind you."}

# print(codes)

actions = ['Back Away', 'Cover our Heads','Take a Photograph']

# birds names
# for key in rarebirds.keys():
#     print("Bird name: ", key)

# aggressive, take cover

# for key, val in rarebirds.items():

#     if (rarebirds[key]["Aggressive"] == True) and (rarebirds[key]["Endangered"] == True):
#         print("Our bird:", key, "\nACTION:", actions[1], "and", actions[0], "\n")
#     elif rarebirds[key]["Endangered"]:
#         print("Our bird:", key, "\nACTION:", actions[0], "\n")
#     elif rarebirds[key]["Aggressive"]:
#         print("Our bird:", key, "\nACTION", actions[1])

# check out your code
# for code in codes:
#     print(code)

for key, val in rarebirds.items():
    rarebirds[key]['seen'] = False

# for key, val in rarebirds[key].items():
#     print(key, val)

"""
Outputs:
Height (m) 2.1
Weight (kg) 70
Color Brown
Endangered False
Aggressive False
seen False
"""

encounter = True

sighting = input("What do you see? ").lower()
rarebirdsList = []

for birds in rarebirds.keys():
    rarebirdsList.append(birds)
if sighting in rarebirdsList:
    print("this is the one!")
else:
    print("sadly, not the one")




### asks user where bird is seen and return code with location
code = int(input("Where do you see it? Input the correct code. "))
location = codes[code]
print("So you've seen a:", sighting, location, "My goodness.")




for key, val in rarebirds.items():

    if (rarebirds[key]["Aggressive"] == True) and (rarebirds[key]["Endangered"] == True):
        print("Our bird:", key, "\nACTION:", actions[1], "and", actions[0], "\n")
    elif rarebirds[key]["Endangered"]:
        print("Our bird:", key, "\nACTION:", actions[0], "\n")
    elif rarebirds[key]["Aggressive"]:
        print("Our bird:", key, "\nACTION", actions[1])
