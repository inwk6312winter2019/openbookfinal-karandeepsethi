fin1=open("Book1.txt")
fin2=open("Book2.txt")
fin3=open("Book3.txt")

def starts_with_vow():
	tup = ("a", "e", "i", "o", "u")
    	d = dict()

    	for line in fin1:
        	line = line.split()
        	for word in line:
            		word = word.strip()
			word=word.split(string.punctuation + string.whitespace)
            		if word[0] in tup:

           			 d[word] = d.get(word, 0) + 1

    	return len(d)
print(starts_with_vow())

