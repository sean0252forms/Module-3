print("3.2.1.15")
# c0=input("Input a number: ")
# steps=0
# evenNumbers=['2','4','6','8','0']
# splitTxt=c0.split()
# print(splitTxt)
# while int(c0)!=1:
# 	for i in evenNumbers:
# 		if splitTxt[-1]==evenNumbers[i]:
# 			continue
# 		else:
# 			c0=3*int(c0)+1
# print(splitTxt)
c0=input("Input a number: ")
steps=0
evenNumbers=['2','4','6','8','0']
splitTxt=list(c0)
c0=splitTxt
newString=''
print(c0)
for i in splitTxt:
	newString+=splitTxt[int(i)]
string2=''
for i in splitTxt:
	string2+=newString[int(i)]
print(string2)
while int(string2)!=1:
	for i in evenNumbers:
		print(i)
	if int(newString[len(newString)-1])==evenNumbers[i]:
			c0=c0 / 2
	else:
			c0=3*int(c0)+1
print(splitTxt)