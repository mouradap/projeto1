import itertools

def generat(fasta):
	for line_num, line in enumerate(file,1):
		yield line.strip()

with open("fasta_seq.fa", 'r') as file:
	fastgen = generat(file)
	#sliceando o generator em uma lista.
	sliced = list(itertools.islice(fastgen, 1))
	print(sliced)
	for line in fastgen:
		print(line)
	print(sliced)