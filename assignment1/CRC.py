
def xor_string(str1,str2):
	result=''
	for counter, value in enumerate(str2):
		if(str1[counter]==value):
			result+='0'
		else:
			result+='1'
		x=counter	
	result+=str1[x+1:]
	return result			

def alter(string,bit):
	if(string[bit-1]=='1'):
		string=string[:bit-1]+'0'+string[bit:]
	else:
		string=string[:bit-1]+'1'+string[bit:]
	return string		
	
def long_Division(message,key):
	result=''
	remainder=message
	while(True):
		if(remainder[0]=='1'):
			result+='1'
			remainder=xor_string(remainder,key)[1:]
		else:
			result+='0'
			remainder=remainder[1:]
		if(len(remainder)<len(key)):
				break;
	remainder=bin(int(remainder,2))[2:]				
	return remainder
		
while(1):
	print ("please type 'generator file_name' to generate the transmitted message in a file named transmitted")
	try:
                
		response = input('')
		if(response.find('.')==-1):
			response=response+".txt"
		pos=response.find(' ')
		file = open(response[pos+1:],'r')
		message=file.readline()[:-1]
		key=file.readline()
		file.close()
		break;
	except FileNotFoundError:
		print('file not found!')	
added_bits=len(key)-1
message=message+'0'*added_bits
remainder=long_Division(message,key)
transmitted_Message=bin(int(message,2)^int(remainder,2))[2:]
file=open('transmitted.txt','+w')
file.write(transmitted_Message+'\n')
file.close()
#print(transmitted_Message)
file=open('transmitted.txt','a')
print ("type v to see if message is correct . \ntype 'a(bit_no)' to alter the message")
response = input('')
if(response=="v"):
	remainder=long_Division(transmitted_Message,key)
	if(remainder=='0'):
		file.write('message is correct!')
	else:
		file.write('message is incorrect!')
if(response.find('a')!=-1):
	bit_no=int(response[response.find('(')+1:response.find(')')])
	altered_Message=alter(transmitted_Message,bit_no)
	print("type v to see if the message is correct")
	response = input('')
	if(response=="v"):
		remainder=long_Division(altered_Message,key)
		if(remainder=='0'):
			file.write('message is correct!')
		else:
			file.write('message is incorrect!')

print("check the transmitted text file \n bye bye")


file.close()

