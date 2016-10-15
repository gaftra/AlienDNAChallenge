def getCuts(cutFile):
	cutFile = open(cutFile, 'r')
	cuts_file = cutFile.read()
	
	# Remove trailing [ and ]
	cuts_file = cuts_file[1:-2]

	unorganised_cuts = cuts_file.split()

	cuts = []
	
	for cut in unorganised_cuts:
		cut = cut.replace('"', '');
		cut = cut.replace(',', '');
		cuts.append(cut)

	return cuts

# Get the end cut from a list
def getEndCut(cut_list, cut_type):
	for cut in cut_list:
		if cut_type == "BC" or cut_type == "DE":
			if cut[-2:] != cut_type:
				return cut
		elif cut_type == "DFAD":
			if cut[-4:] != cut_type:
				return cut
		elif cut_type == "EDA":
			if cut[-3:] != cut_type:
				return cut
	return ""

# Swaps the location of two cuts in a list
def swapCuts(cut_list, indexA, indexB):
	temp = cut_list[indexA]
	cut_list[indexA] = cut_list[indexB]
	cut_list[indexB] = temp

# Gets the number of characters in a list
def numChars(cut_sublist):
	total = 0
	for cut in cut_sublist:
		total += len(cut)

	return total

def tupleState():
	list_cuts = [cuts_BC, cuts_DE, cuts_DFAD, cuts_EDA]
	list_strings = [sorted_BC, sorted_DE, sorted_DFAD, sorted_EDA]
	state = (list_cuts, list_strings)
	return state	

def dynamicCompare(str1, str2):
	if str1[-1] == str2[-1]:
		str3 = str1[:-1]
		str4 = str2[:-1]

		if str3 == '' or str4 == '':
			return true
		else:
			return dynamicCompare(str3, str4)

def getSameCharacters(str1, str2):
	
	str3 = str1[:-1]
	str4 = str2[:-1]

	if str3 == '' or str4 == '':
		return 1

	if str1[-1] == str2[-1]:
			return getSameCharacters(str3,str4) - 1
	else:
			return 1 + getSameCharacters(str3,str4)

def getDiffCharacters(str1,str2):
	if (len(str1) < len(str2)):
		return len(str1) - getSameCharacters(str1, str2)
	else:
		return len(str2) - getSameCharacters(str1,str2)
