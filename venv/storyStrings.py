import textwrap # a regex module used to split the story strings into new lines

# --------------------------------------------------------------------------------------------------------------------
# --------------- declarations ---------------------------------------------------------------------------------------
# below a dictionary declaration
# there are seven entries - each one for every line on the game screen
gameScreenStringDictionary = {'string0': '', 'string1': '','string2': '','string3': '','string4': '','string5': '',
                              'string6': '', 'left': '', 'right': ''}
# ---------------------------------------------------------------------------------------------------------------------

#
# --------------------------------------------------------------------------------------------------------------------
# -------- a rejected function ---------------------------------------------------------------------------------------
# def stringChopper (stringToChop): # a function that slices the string into string displayed on one of the seven lines
#     j = 0 # a counter used to point to a specific entry in the dictionary
#     global gameScreenStringDictionary # accessing the global dictionary - function returns implicitly
#     if len(stringToChop) > 95: # for strings longer than one line
#         for i in range (0, len(stringToChop),95): # chop to 95 characters max
#             gameScreenStringDictionary["string{}".format(j)] = stringToChop[i: i+95]
#             j+=1
#     elif len(stringToChop) <= 95: # for short strings
#         gameScreenStringDictionary["string0"] = stringToChop
# --------------------------------------------------------------------------------------------------------------------




# --------------------------------------------------------------------------------------------------------------------
def stringChopper (stringToChop, leftChoice, rightChoice): # a function that slices the string into string displayed on one of the seven lines
    j = 0 # a counter used to point to a specific entry in the dictionary
    global gameScreenStringDictionary # accessing the global dictionary - function returns implicitly
    if len(stringToChop) > 95: # for strings longer than one line
        gameScreenStringDictionary["left"] = leftChoice
        gameScreenStringDictionary["right"] = rightChoice
        choppedStringList = textwrap.wrap(stringToChop, width=95) # using the text wrap to return list of lines
        for stringLine in choppedStringList: # assign entries from the generated list to the dictionary
            gameScreenStringDictionary["string{}".format(j)] = stringLine
            j += 1
    elif len(stringToChop) <= 95: # for short strings just assign to the first dictionary entry
        gameScreenStringDictionary["string0"] = stringToChop
        gameScreenStringDictionary["left"] = leftChoice
        gameScreenStringDictionary["right"] = rightChoice
# --------------------------------------------------------------------------------------------------------------------





# ----------------------------------------------------------------------------------------------------------
# strings used to test the stringChopper
# ------------------ strings source: https://en.wikipedia.org/wiki/Iliad
#testString = "Although the story covers only a few weeks in the final year of the war, the Iliad mentions or alludes to many of the Greek legends about the siege; the earlier events, such as the gathering of warriors for the siege, the cause of the war, and related concerns tend to appear near the beginning. Then the epic narrative takes up events prophesied for the future, such as Achilles' imminent death and the fall of Troy, although the narrative ends before these events take place. However, as these events are prefigured and alluded to more and more vividly, when it reaches an end the poem has told a more or less complete tale of the Trojan War."  # a test run
#testString = "After nine days of plague, Achilles, the leader of the Myrmidon contingent, calls an assembly to deal with the problem. Under pressure, Agamemnon agrees to return Chryseis to her father, but decides to take Achilles' captive, Brisēís, as compensation. Angered, Achilles declares that he and his men will no longer fight for Agamemnon and will go home. Odysseus takes a ship and returns Chryseis to her father, whereupon Apollo ends the plague."
testString = " Achilles relents and lends Patroclus his armor, but sends him off with a stern admonition not to pursue the Trojans, lest he take Achilles' glory. Patroclus leads the Myrmidons into battle and arrives as the Trojans set fire to the first ships. The Trojans are routed by the sudden onslaught, and Patroclus begins his assault by killing Zeus's son Sarpedon, a leading ally of the Trojans. Patroclus, ignoring Achilles' command, pursues and reaches the gates of Troy, where Apollo himself stops him. Patroclus is set upon by Apollo and Euphorbos, and is finally killed by Hector. "
testLeft = "passing left"
testRight = "passing right"
stringChopper(testString, testLeft, testRight)
#-----------------------------------------------------------------------------------------------------------




# -----------------------------------------------------------------------------------------------------------
# passing the chopped strings to the main class
string0 = gameScreenStringDictionary['string0']                # should the dictionary be cleaned before next screen?
string1 = gameScreenStringDictionary['string1']
string2 = gameScreenStringDictionary['string2']
string3 = gameScreenStringDictionary['string3']
string4 = gameScreenStringDictionary['string4']
string5 = gameScreenStringDictionary['string5']
string6 = gameScreenStringDictionary['string6']
left = gameScreenStringDictionary['left']
right = gameScreenStringDictionary['right']
# -----------------------------------------------------------------------------------------------------------