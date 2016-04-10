def compression(input1):
	result = ""
	length = len(input1)
	cnt = 1
	i =1

	if length==0:
		return ""
	elif length==1:
		return input1+"1"

	else:
		while i<length:
			if input1[i]==input1[i-1]:
				cnt+=1
			else:
				result=result+input1[i-1]+str(cnt)
				cnt=1

			i+=1

		result=result+input1[i-1]+str(cnt)
		return result


print (compression("AAAAabcc"))