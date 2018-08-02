string=input()
count=0
num=string.find('bob')
while num>=0:
	count=count+1
	num=string.find('bob',num+2)
print(count)