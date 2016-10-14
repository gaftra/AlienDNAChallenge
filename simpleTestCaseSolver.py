def getChromosomes(cutFile):
	chromosomes_file = cutFile.read()
	
	# Remove trailing [ and ]
	chromosomes_file = chromosomes_file[1:-2]

	unorganised_chromosomes = chromosomes_file.split()

	chromosomes = []
	
	for chromosome in unorganised_chromosomes:
		chromosome = chromosome.replace('"', '');
		chromosome = chromosome.replace(',', '');
		chromosomes.append(chromosome)

	return chromosomes

# Get the end chromosome from a list
def getEndChromosome(chromosome_list, cut_type):
	for chromosome in chromosome_list:
		if chromosome[-2:] != cut_type:
			chromosome_list.remove(chromosome)
			return chromosome
	return ""

# Search appropriate file for largest sequence ending in Sn
def searchSn(list_type, sn):
	chromosomes_list = []
	if list_type == "AB":
		chromosomes_list = chromosomes_AB 
	elif list_type == "BA":
		chromosomes_list = chromosomes_BA
	elif list_type == "CB":
		chromosomes_list = chromosomes_CB
	else:
		print "Invalid list type"
		return []	

	# Search the list of chromosomes for sequences ending in sn
	possible_sequences = []
	for chromosome in chromosomes_list:	
		if chromosome.endswith(sn):
			possible_sequences.append(chromosome);

	# Get the largest sequence in the list
	max_sequence = ""
	max_num = 0

	for sequence in possible_sequences:
		if len(sequence) > max_num:
			max_num	= len(sequence)
			max_sequence = sequence

	return max_sequence

filename_AB = "simpleTestCases/10_cut_AB"
filename_BA = "simpleTestCases/10_cut_BA"
filename_CB = "simpleTestCases/10_cut_CB"

file_AB = open(filename_AB, "r")
file_BA = open(filename_BA, "r")
file_CB = open(filename_CB, "r")

chromosomes_AB = getChromosomes(file_AB);
chromosomes_BA = getChromosomes(file_BA); 
chromosomes_CB = getChromosomes(file_CB);

cuts = []
cuts.append("AB")
cuts.append("BA")
cuts.append("CB")

n = getEndChromosome(chromosomes_CB, "CB")

print "n: " + n;

# Scan n for first instance of a cut
beginningLoc = 0
endingLoc = 2
cutType = ""

for x in range(1, len(n)):
	section = n[beginningLoc:endingLoc]

	if section == "AB":
		cutType = "AB"
		break
	elif section == "BA":
		cutType = "BA"
		break
	elif section == "CB":
		cutType = "CB"	
		break
	else:
		beginningLoc += 1
		endingLoc += 1

# If we do not find another cut within the string, abandon all hope
if cutType == "":
	print "CUT NOT FOUND ABANDON SHIP"
	exit(0)	

sn = n[:endingLoc]
inv_sn = n[endingLoc:]

print "Sn: " + sn
print "inv_sn: " + inv_sn


print "AB file results: "
print searchSn(cutType, sn)

new_string = searchSn(cutType, sn) + inv_sn

print "Original Genome: " + new_string
