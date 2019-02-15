fin=open("Book1.txt")
fin1=open("Book2.txt")
fin2=opn("Book3.txt")

def unique_words():
	a_list=[]
	b_list=[]
	c_list=[]
	d1={}
	d2={}
	d3={}
	for line in fin:
		for words in line:
			words=line.strip()
			words=line.split(".")
			d1[words]=d1.get[words,0]+1
			a_list.append[words]
	for line in fin1:
                for words in line:
                        words=line.strip()
                        words=line.split(".")
                        d2[words]=d2.get[words,0]+1
                        b_list.append[words]

	for line in fin2:
                for words in line:
                        words=line.strip()
                        words=line.split(".")
                        d3[words]=d3.get[words,0]+1
                        c_list.append[words]

print(unique_words())


