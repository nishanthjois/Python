def unqiuechars2(s):

	char = set()

	for ch in s:
		if ch in char:
			return False
		
		else:
			char.add(ch)

	return True

res= unqiuechars2('abcss')
print (res)
# print (uniquechars2('abcd'))
# print (uniquechars2('abcda'))
# print (uniquechars1('abcd'))
# print (uniquechars1('abcda'))

