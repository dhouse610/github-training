mainstring = """All happy families are alike; each unhappy family is unhappy in its own way. All was confusion in the Oblonskys’ house. The wife had found out that the husband was having an affair with their former French governess, and had announced to the husband that she could not live in the same house with him. This situation had continued for three days now, and was painfully felt by the couple themselves, as well as by all members of the family and household.   They felt that there was no sense in their living together and that people who meet accidentally at any inn have more connection with each other than they, the members of the family and household of the Oblonskys . The wife would not leave her rooms, the husband was away for the third day. The children were running all over the house as if lost; the English governess quarreled with the housekeeper and wrote a note to a friend, asking her to find her a new place; the cook had already left the premises the day before, at dinner-time; the kitchen-maid and coachman had given notice."""

list_of_strings = str.split(mainstring,".")

for i in range(len(list_of_strings)):
    exec(f'string_var_{i} = list_of_strings[i]')

string_vars = [string_var_0, string_var_1, string_var_2, string_var_3, string_var_4, string_var_5, string_var_6, string_var_7]

###Lowercase###
string_var_0_lower = str.lower(string_var_0)
###Uppercase###
string_var_0_upper = str.upper(string_var_0)

###Reverse Letters###
def Reverse(sentence):
    wordlist = str.split(sentence," ")
    revlist = []
    for i in range(len(wordlist)):
        wordlist[i] = wordlist[i][::-1]
        revlist.append(wordlist[i])
    return " ".join(revlist)
string_var_0_rev = Reverse(string_var_0)

###length###
length = len(string_var_0)
lengthL = len(str.lstrip(string_var_0))
lengthR = len(str.rstrip(string_var_0))
#print(length,lengthL,lengthR)


###Alternating Letters###
words = str.strip(string_var_0," ")
evenlist = words[2::2]
oddlist = words[1::2]
evenoddlist = []
evenoddlist.append(evenlist)
evenoddlist.append(oddlist)

###Replacing###
string_var_0_rep = string_var_0.replace("a","x")
string_var_0_rep1 = string_var_0.replace("families","pythons")


finallist = [string_var_0, string_var_1, string_var_2, string_var_3, string_var_4, string_var_5, string_var_6, string_var_7]
finallist1 = [string_var_0, string_var_1, string_var_2, string_var_3, string_var_4, string_var_5, string_var_6]
newparagraph = ".".join(finallist)
newparagraph1 = ".".join(finallist1)
