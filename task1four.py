import string
fin=open("Book1.txt")
def character_word_count():

    d = dict()
    for line in fin:
        line = line.split()
        for word in line:
            word = word.strip()
	    word = word.split(string.punctuation+string.whitespace)
            d[word] = len(word)
    return d

print(character_word_count())
