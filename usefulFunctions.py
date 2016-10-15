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

