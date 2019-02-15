import string
fin1=open("Book1.txt")
fin2=open("Book2.txt")
fin3=open("Book3.txt")

def top_twenty():
	d1=dict()
	d2=dict()
	d3=dict()

	for line in fin1:
		line=line.strip()
		line=lin.split(string.punctuation+string.whitespace)
		d1[word] = d1.get(word,0) + 1
	return d1

	for line in fin2:
                line=line.strip()
                line=lin.split(string.punctuation+string.whitespace)
        	d2[word] = d2.get(word,0) + 1
	return d2

	for line in fin3
                line=line.strip()
                line=lin.split(string.punctuation+string.whitespace)
        	d3[word] = d3.get(word,0) + 1
	return d3

		for a in d1 and b in d2 and c in d3:
			if a[20] == b[20] == c[20]
				return dict(a,b,c)
			else:
				break

print(top_twenty())
