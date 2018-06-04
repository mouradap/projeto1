import pickle
import itertools


#Nao era necessario transformar o arquivo fasta em gen. Apenas o resultado da buscar por yield ao inves de uma lista.
# def generat(fasta):
# 	with open(fasta, 'r') as file:
# 		for line_num, line in enumerate(file,1):
# 			yield line.strip()

def search(fasta, start, end, gene_name):
	index = pickle.load(open(fasta + '.fai', 'rb'))

	seq = ''

	for line_num, line in enumerate(fasta,1):

		if line_num in index[gene_name].keys():
			if start >= index[gene_name][line_num][0] and start <= index[gene_name][line_num][1]:
				start_pos = start - index[gene_name][line_num][0]
				print(start_pos)

				if end <= index[gene_name][line_num][1]:
					end_pos = end + index[gene_name][line_num][0] -1
					print(end_pos)
					seq = line[start_pos, end_pos]
					break

				elif end > (index[gene_name][line_num][1]):
					end_pos = end - index[gene_name][line_num][1]
					seq = line[start_pos:]

			if start < index[gene_name][line_num][0]:
				if end > index[gene_name][line_num][1]:
					seq = line[:]

				elif end <= index[gene_name][line_num][0]:
					end_pos = end - index[gene_name][line_num][0]
					seq = line[:end_pos]
					yield seq
					break
	# 		else:
	# 			seq = tuple(index[gene_name][line_num])

	# return seq

		if len(seq) > 0:
			yield seq

def len(fasta, gene_name=None):
    index = pickle.load(open(fasta + '.fai', "rb"))

    if gene_name is None:

        for name in index.keys():
            last_index_line = sorted(index[name].keys())[-1] # key of the last line of the index file
            print(name, index[name][last_index_line][1])

    # Get the index[1] of the last tuple of the last line
    else:
        last_index_line = sorted(index[gene_name].keys())[-1]
        print(gene_name, index[gene_name][last_index_line][1])