import string
message = input('enter the message: ').replace(' ','').lower()

key = int(input('enter the encrypted key: '))

alphabet_string = string.ascii_lowercase #for get all alphabet
alphabet_position  = {};
positon_alphabet ={}
count = int(0)
for letter in alphabet_string:
    alphabet_position[letter] = count
    positon_alphabet[count] = letter
    count+=1

#print(positon_alphabet)
#print(alphabet_position)

#for cipher text
cipherText=''
for i in range(0,len(message)):
    if(message[i]>='a' and message[i]<='z'):
      pos = (alphabet_position[message[i]]+key)%26
      cipherText+= positon_alphabet[pos]
    else :
        cipherText+=' '
print('the cipher text is : ',cipherText.upper())

plainText=''
for i in range(0,len(cipherText)):
    if(cipherText[i]>='a' and cipherText[i]<='z'):
        pos = (alphabet_position[cipherText[i]]-key)%26
        plainText+= positon_alphabet[pos]
    else :
        plainText+=' '    
print(f'the plain text is: {plainText.upper()}')
