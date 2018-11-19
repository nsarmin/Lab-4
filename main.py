from chaininghashtable import ChainingHashTable
from Node import Word

chainTable= ChainingHashTable(27*27*27*27)

f=open ('glove.6B.50d.txt', encoding= "utf8")
line= f.readline()

while line:
    thisline= line.split(" ")
    word= thisline[0]
    Array= []
    for j in range(1, len(thisline)):
        Array.append(float(thisline[j]))
    node= Word (word, Array)
    chainTable.insert(node)
    line=f.readline()
f.close()

chainTable.Avrg_comparisons()
#compute the load_factor hashtabe
chainTable.load_factor()

print ("\nComparing Table: ")
f=open('compare.appendix.txt')
line=f.readline()

while line:
	thisline=line.split(" ")
	
	word_0 = thisline[0]
	word_0 = chainTable.search(word_0)
	
	word_1 = thisline[1]
	word_1 = chainTable.search(word_1)
	
	if word_0 is None or word_1 is None:
		print (thisline[0]+ " or " + thisline[1]+ " --Unique--")
	else:
		A_0= word_0.get_embed()
		A_1= word_1.get_embed()
		dot_product= 0
		x_0, x_1= 0,0
		for i in range (len(A_0)):
			dot_product += A_0[i]*A_1[i]
			x_0 += A_0[i]* A_0[i]
			x_1 += A_1[i]* A_1[i]
	
		x_To = (x_0**.5)*(x_1**.5)
		Calc=dot_product/x_To
		print (thisline[0],"",thisline[1], "", Calc)
	line=f.readline()
