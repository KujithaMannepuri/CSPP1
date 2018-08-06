'''
Replace all the special characters(!, @, #, $, %, ^, &, *) in a given string with a space.
example : ab!@#cd is the input, the output is ab   cd
Output has three spaces, which are to be replaced with these special characters
'''
def main():
    '''
    Read string from the input, store it in variable str_input.
    '''
    str1=input()
    str2=" "
    l1=len(string)
    temp=[]
    for i in range(0,l1,1):
    	if str1[i]==['!','@','#','$','%','^','&','*']:
    		temp=str2
    		str1[i]=temp
    	print(str1)



if __name__ == "__main__":
    main()
