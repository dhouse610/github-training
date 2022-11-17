###Exercise 1 for Python###

print("Hello World")

handle = "Moral wounds have this peculiarity - they may be hidden, but they never close; always painful, always ready to bleed when touched, they remain fresh and open in the heart"

counts = dict()

words = handle.split()
for word in words:
    counts[word] = counts.get(word,0) + 1

bigcount = None
bigword = None
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count

print(bigword, bigcount)
