import pickle
import itertools

def generat(fasta):
	with open(fasta, 'r') as file:
		for line_num, line in enumerate(file,1):
			yield line.strip()

def slicer(fasta, generator, ranging, gene_name):
	index = pickle.load(open(fasta + '.fai', 'rb'))

	slices = []

	strings = ranging.replace('-',' ').split(' ')
	strings = list(map(int, strings))
	# print(strings)

	genstr = (i for i in strings)

	# for i in genstr:
	# 	print(i + next(genstr))

	for i in genstr:
		prox = next(genstr)
		for line_num, line in enumerate(generator,1):

			if line_num in index[gene_name].keys():
				if i >= index[gene_name][line_num][0] and i <= index[gene_name][line_num][1]:
					start_pos = i - index[gene_name][line_num][0] +1
					print(start_pos)

					if prox <= index[gene_name][line_num][1]:
						end_pos = prox + index[gene_name][line_num][0] -1
						print(end_pos)
						slices += tuple(itertools.islice(line, start_pos, end_pos))
						continue

					elif prox > (index[gene_name][line_num][1]):
						slices += tuple(itertools.islice(line, start_pos, ))
						continue

				if i < index[gene_name][line_num][0]:
					if prox > index[gene_name][line_num][1]:
						slices += tuple(line)
						continue

					elif prox <= index[gene_name][line_num][0]:
						end_pos = prox - index[gene_name][line_num][0]
						slices += tuple(line[:end_pos])
						continue
		continue

	return slices

# import pickle
# import itertools

# def splicing(generator, ranging, gene):
# 	index = pickle.load(open(fasta + '.fai', 'rb'))
# 	ranges = ranging.replace('-',',').split(" ")
# 	slices = []
# 	for item in ranges:
# 		for line_num, line in enumerate(generator,1):

# 			if line_num in index[gene_name].keys():
# 				if ranges[] >= index[gene_name][line_num][0] and ranges <= index[gene_name][line_num][1]:
# 					start_pos = start - index[gene_name][line_num][0]
# 					print(start_pos)

# 					if end <= index[gene_name][line_num][1]:
# 						end_pos = end + index[gene_name][line_num][0] -1
# 						print(end_pos)
# 						seq = tuple(itertools.islice(line, start_pos, end_pos))
# 						break

# 					elif end > (index[gene_name][line_num][1]):
# 						seq = tuple(itertools.islice(line, start_pos, ))

# 				if start < index[gene_name][line_num][0]:
# 					if end > index[gene_name][line_num][1]:
# 						seq += tuple(line)

# 					elif end <= index[gene_name][line_num][0]:
# 						end_pos = end - index[gene_name][line_num][0]
# 						seq += tuple(line[:end_pos])
# 						break

# 	return slices