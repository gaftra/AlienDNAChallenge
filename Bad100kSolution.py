#Solves the 100k genome using a horrible method

def find_initial(file_BC, file_DE, file_EDA, file_DFAD):
    bc_diff = ""
    for element in file_BC:
        element = element[1:-1]
        if element[-2:] != "BC":
            bc_diff = element
            break
    de_diff = ""
    for element in file_DE:
        element = element[1:-1]
        if element[-2:] != "DE":
            de_diff = element
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
    ar = [bc_diff, de_diff, dfad_dif, eda_dif]
    longest = 0
    best_cut = ""
    for x in range(len(ar)):
        cur_x = ar[x]  # bc_diff
        if len(cur_x) > longest:
            longest = len(cur_x)
            best_cut = cur_x.partition("_")[0].upper()
    return (longest, best_cut)


def find_first_next_cut(sequence):
    mini = ["",999999999999]
    ar = ["BC", "DE", "DFAD", "EDA"]
    for x in range(4):
        try:
           first = sequence.index(ar[x])
           if first < mini[1]:
               mini[1] = first
               mini[0] = ar[x]
        except ValueError:
           pass
    return mini[0],sequence[:mini[1]]+mini[0]

def find_first_v2(cut,sequence):
	try:
		first = sequence.index(cut)
	except ValueError:
		return cut,None
	return cut,sequence[:first]+cut

def findMatch(file_array,sequence,n,c):
	out = []
	for x in file_array:
		x = x[1:-1]
		if (x[-(len(sequence)):] == sequence):
			out.append(x[:len(x)-len(sequence)])
	for o in out:
		if c < 300:
			main(o+n,c+1)
	
file_BC = open("genomePieces/100k_digest_BC", "r")
file_DE = open("genomePieces/100k_digest_DE", "r")
file_DFAD = open("genomePieces/100k_digest_DFAD", "r")
file_EDA = open("genomePieces/100k_digest_EDA", "r")
file_arrayBC = file_BC.readline()[1:-1].split(", ")
file_arrayDE = file_DE.readline()[1:-1].split(", ")
file_arrayDFAD = file_DFAD.readline()[1:-1].split(", ")
file_arrayEDA = file_EDA.readline()[1:-1].split(", ")

# find initial unique ending/sequence and its length
# best_cut ^; best_len - its 
import sys
best_len, best_cut = find_initial(file_arrayBC, file_arrayDE, file_arrayEDA, file_arrayDFAD)
global_sequence_length = best_len
n = best_cut

def main(n,c):
	if len(n) > 100000:
		return "Fail"
	if len(n) == 100000:
		print n, len(n)
		file = open('100k_answer','w')
		file.write(n)
		sys.exit()
		
		return True
	ar = ["EDA","BC","DE","DFAD"]
	sn = find_first_v2(ar[c%4],n)
	
	if sn[0] == "BC" and sn[1] != None:
		print len(n)
		findMatch(file_arrayBC,sn[1],n,c)
	if sn[0] == "DE" and sn[1] != None:
		print len(n)
		findMatch(file_arrayDE,sn[1],n,c)
	if sn[0] == "DFAD" and sn[1] != None:
		print len(n)
		findMatch(file_arrayDFAD,sn[1],n,c)
	if sn[0] == "EDA" and sn[1] != None:
		print len(n)
		findMatch(file_arrayEDA,sn[1],n,c)
	
main(n,0)
