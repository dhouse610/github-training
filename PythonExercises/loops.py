import urllib.request  

wordDict = {}

poem = ""
for line in urllib.request.urlopen('https://www.cs.cmu.edu/~dst/DeCSS/Gallery/decss-haiku.txt'):
    poem = poem + line.decode()

poem = poem.replace('\n', ' ')

###loop test###
count = 0
while count < 8:
    print("Python is awesome")
    count += 1

counts = dict()

poemlist = poem.split()
for word in poemlist:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

thirds = int(len(poemlist)/3)
startStops = [[0, thirds], [thirds, thirds * 2], [(thirds * 2), len(poemlist)]]

longestWords = []
for ranges in startStops:
    i = ranges[0]
    longWord, wordindex = '', 0
    while i < ranges[1]:
        if len(poemlist[i]) > len(longWord):
            longWord = poemlist[i]
            wordindex = i
        i += 1
    longestWords.append([wordindex, longWord])
    
print(longestWords)
print(poemlist[longestWords[0][0]])
print(poemlist[longestWords[1][0]])
print(poemlist[longestWords[2][0]])

for i in longestWords:
    print(i[1] == poemlist[i[0]])


testlist = ['123','1234','1234']
word = max(testlist,key=len)
index = testlist.index(word)
print(word,index)