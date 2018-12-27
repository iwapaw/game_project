

# below a dictionary declaration
# there are seven entries - each one for every line on the game screen
gameScreenStringDictionary = {'string0': '', 'string1': '','string2': '','string3': '','string4': '','string5': '',
                              'string6': ''}
# ---------------------------------------------------------------------------------------------------------------------

def stringChopper (stringToChop): # a function that slices the string into string displayed on one of the seven lines
    j = 0 # a counter used to point to a specific entry in the dictionary
    global gameScreenStringDictionary # accessing the global dictionary - function returns implicitly
    if len(stringToChop) > 95: # for strings longer than one line
        for i in range (0, len(stringToChop),95): # chop to 95 characters max
            gameScreenStringDictionary["string{}".format(j)] = stringToChop[i: i+95]
            j+=1
    elif len(stringToChop) <= 95: # for short strings
        gameScreenStringDictionary["string0"] = stringToChop


testString = "game story body "  # a test run
stringChopper(testString)


# -----------------------------------------------------------------------------------------------------------
# passing the chopped strings to the main class
string0 = gameScreenStringDictionary['string0']
string1 = gameScreenStringDictionary['string1']
string2 = gameScreenStringDictionary['string2']
string3 = gameScreenStringDictionary['string3']
string4 = gameScreenStringDictionary['string4']
string5 = gameScreenStringDictionary['string5']
string6 = gameScreenStringDictionary['string6']
left = "left test"
right = "test right"