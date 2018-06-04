stringue = "1-20 30-40 50-60"
strings = stringue.replace('-',' ').split(' ')
print(strings)

frase="asodjnqwod,q[w,djasdjnqwpokdaksmdjqjwmdpals,djqwdmlas;dkaopwjqnkldmal;smdoqwndkasda"
strings = list(map(int, strings))
print(strings)

genstr = (i for i in strings)

for i in genstr:
	print(frase[i-1:next(genstr)])
	# print(frase[next(genstr):next(genstr)])

# for i in genstr:
# 	print(frase[i] + frase[next(i)])



# print(frase[int(strings[0]):int(strings[1])])