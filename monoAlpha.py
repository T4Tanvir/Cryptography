from random import shuffle
import string

message = input('enter the message: ').replace(' ','')


alphabet_sequence = string.ascii_lowercase
alphabetList =[]
suffleAlphabetList=[]
for i in range(0,len(alphabet_sequence)):
    alphabetList.append(alphabet_sequence[i])
    suffleAlphabetList.append(alphabet_sequence[i])


shuffle(suffleAlphabetList)

alpha_to_cipher = {}
cipher_to_alpha = {}

count = int(0)
for lettr in suffleAlphabetList:
    alpha_to_cipher[alphabetList[count]] = lettr
    cipher_to_alpha[lettr] = alphabetList[count]
    count+=1
print(' ')
print('alphabet to cipher replacement ')

print(alpha_to_cipher)
print(' ')
#for cipher text
cipher_text=''
for char in range(0,len(message)):
   
    if message[char]>='a' and message[char]<='z': 
        cipher_text += alpha_to_cipher[message[char]]
    else :
        cipher_text+=' '
print(f'the cipher text: {cipher_text.upper()}')
#for plain text
plain_text=''
for char in range(0,len(cipher_text)):
   
    if cipher_text[char]>='a' and cipher_text[char]<='z': 
        plain_text += cipher_to_alpha[cipher_text[char]]
    else :
        plain_text+=' '
print(f'the plain text: {plain_text.upper()}')