
def encryptMod(stringToEnc,shift):
	alphabet,brokenString,out=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'.lower()),stringToEnc.split(' '),''
	for i in brokenString:
		a=list(i.lower())
		for j in range(len(a)):
			if a[j] in alphabet:
				b=alphabet.index(a[j].lower())
				if (b+shift)>len(alphabet)-1: b=(b+shift)-len(alphabet)
				else:b=b+shift
				out+=alphabet[b]
			else:
				out+=a[j]
		out+=' '
	return out
def encrypt(stringToEnc):
	alphabet,brokenString,out=list('ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'.lower()),stringToEnc.split(' '),''
	for i in brokenString:
		a=list(i)
		for j in range(len(a)):
			b=alphabet.index(a[j].lower())
			if (b+3)>len(alphabet)-1: b=(b+3)-len(alphabet)
			else:b=b+3
			out+=alphabet[b]
		out+=' '
	return out



