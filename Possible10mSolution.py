#Solves 150k of the 10m gneome using a half-decent method

#This function returns the largest ending string from the four digest files by searching for the string in the file
#which does not end in the given 'cut' substring. The largest of these strings is then returned.
def find_initial(file_BC, file_DE, file_EDA, file_DFAD, file_ABB):
    bc_diff = ""											#Set diff to empty string
    for element in file_BC:									#For each element in the file:
        element = element[1:-1]								#	Strip the element of quotation marks
        if element[-2:] != "BC":							#	If the element does not end in the cut:
            bc_diff = element								#		set diff to that element
            break											#		break the loop
    de_diff = ""
    for element in file_DE:
        element = element[1:-1]
        if element[-2:] != "DE":
            de_diff = element
            break
    abb_dif = ""
    for element in file_ABB:
        element = element[1:-1]
        if element[-3:] != "ABB":
            abb_diff = element
            break
    eda_dif = ""
    for element in file_EDA:
        element = element[1:-1]
        if element[-3:] != "EDA":
            eda_dif = element
            break
    dfad_dif = ""
    for element in file_DFAD:
        element = element[1:-1]
        if element[-4:] != "DFAD":
            dfad_dif = element
            break
    ar = [bc_diff, de_diff, abb_diff, dfad_dif, eda_dif]
    longest = 0												#Set "longest" to 0
    best_cut = ""											#Set best_cut to ""
    for x in range(len(ar)):								#For each of the four ending strings:
        cur_x = ar[x]  			
        if len(cur_x) > longest:							#If the length of the string > 'longest':
            longest = len(cur_x)							#	Set 'longest' to the size of the string
            best_cut = cur_x.partition("_")[0].upper()		#	Set best_cut to the string
    return (longest, best_cut)								#Return the max sized ending string and its length


#This function takes in a sequence as well as a 'cut' substring, and strips everything to the right of the first occurence of the cut.
def find_first_next_cut(cut,sequence):
	try:
		first = sequence.index(cut)							#Set 'first' to the index of the first occurence of 'cut'
	except ValueError:										#If the cut doesn't exist in the sequence:
		return ""											#	Return empty string
	return sequence[:first]+cut								#Return the stripped verison of the sequence

#This function finds all possible chromosomes in the given digest file that can 'fit' into the input sequence.
def findMatch(file_array,sequence):
	output = []
	for chromosome in file_array:														#For each chromosome in the file:
		chromosome = chromosome[1:-1]													#	Strip the quotation marks
		if (chromosome[-(len(sequence)):] == sequence):									#	If the last n characters of the chromosome is identical to the sequence where n is the length of the sequence:
			output.append([chromosome[:len(chromosome)-len(sequence)],chromosome])		#		Append the chromosome, but with the sequence removed from the right-most part of the string, to the output list, as well as the full chromosome
	return len(output),output															#	Return the output list as well as its length

#Parsing the digest files
file_BC = open("genomePieces/10m_digest_BC", "r")
file_DE = open("genomePieces/10m_digest_DE", "r")
file_ABB = open("genomePieces/10m_digest_ABB.txt", "r")
file_DFAD = open("genomePieces/10m_digest_DFAD", "r")
file_EDA = open("genomePieces/10m_digest_EDA", "r")
file_arrayBC = file_BC.readline()[1:-1].split(", ")
file_arrayDE = file_DE.readline()[1:-1].split(", ")
file_arrayABB = file_ABB.readline()[1:-1].split(", ")
file_arrayDFAD = file_DFAD.readline()[1:-1].split(", ")
file_arrayEDA = file_EDA.readline()[1:-1].split(", ")

#Get the longest ending string from the digest files and their length
best_len, best_cut = find_initial(file_arrayBC, file_arrayDE, file_arrayEDA, file_arrayDFAD, file_arrayABB)
global_sequence_length = best_len

#n is the variable used to store the full genome sequence.
n = best_cut

def main(n,BC,DE,DFAD,EDA,ABB):

	#We loop the program 100 times, as it takes ~100 iterations to reach our stopping point.
	while len(n) < 10000000:
	
		#If the length of the genome exceeds the length limit, something has gone terribly wrong and we need to kill it to end its suffering.
		if len(n) > 100000000:
			print "Fail"
			return
	
		#Keep track of the current length of n
		print "Length", len(n)
	
		#The following algorithm is used for each of the four digest files:
		
		#set 'next_cut' to a substring of n where everything to the right of the appropriate cut is removed.
		#set 'matchOutput' to a list of all possible chromosomes that could be added to the genome.
		#print the cut and number of possibilities to keep track of the program.
		#if only one possibility exists:
		#	delete that possibility from the digest file so it cannot be duplicated in a later iteration
		#	add it to the left of n, sliced appropriately so it fits into the genome.
		
		next_cut_DFAD = find_first_next_cut("DFAD",n)	
		matchOutput = findMatch(DFAD,next_cut_DFAD)	
		print "DFAD", matchOutput[0]
		if matchOutput[0] == 1:
			delString = '"' + matchOutput[1][0][1] + '"'		
			DFAD.remove(delString)
			n = matchOutput[1][0][0] + n
			
		next_cut_EDA = find_first_next_cut("EDA",n)
		matchOutput = findMatch(EDA,next_cut_EDA)
		print "EDA", matchOutput[0]
		if matchOutput[0] == 1:
			delString = '"' + matchOutput[1][0][1] + '"'		
			EDA.remove(delString)
			n = matchOutput[1][0][0] + n
			
		next_cut_BC = find_first_next_cut("BC",n)
		matchOutput = findMatch(BC,next_cut_BC)
		print "BC", matchOutput[0]
		if matchOutput[0] == 1:
			delString = '"' + matchOutput[1][0][1] + '"'
			BC.remove(delString)
			n = matchOutput[1][0][0] + n
			
		next_cut_DE = find_first_next_cut("DE",n)	
		matchOutput = findMatch(DE,next_cut_DE)
		print "DE", matchOutput[0]
		if matchOutput[0] == 1:
			delString = '"' + matchOutput[1][0][1] + '"'
			DE.remove(delString)
			n = matchOutput[1][0][0] + n

		next_cut_ABB = find_first_next_cut("ABB",n)
		matchOutput = findMatch(ABB,next_cut_ABB)
		print "ABB", matchOutput[0]
		if matchOutput[0] == 1:
			delString = '"' + matchOutput[1][0][1] + '"'		
			ABB.remove(delString)
			n = matchOutput[1][0][0] + n
			
		
		file = open('10mAnswer_2.txt','w')
		file.write(n)
		file.close
	#After the 100 iterations, save the genome sequence to a file.
	
	file = open('10mAnswer.txt','w')
	file.write(n)
	file.close


main(n,file_arrayBC,file_arrayDE,file_arrayDFAD,file_arrayEDA, file_arrayABB)
