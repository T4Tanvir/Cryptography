import math
import string

message = input('enter the message: ').lower()
key = input('enter the key: ');

alphabet_sequence = string.ascii_lowercase
alphabet_position = {}
position_alphabet = {}
for i in range(0,26):
    alphabet_position[alphabet_sequence[i]]=i
    position_alphabet[i] = alphabet_sequence[i]

repeatKey_positon={}
key_length=len(key)
for i in range(0,26):
    repeatKey_positon[i]=key[i%key_length]
    
#for cipher text
cipher_text=''
for i in range(0,len(message)):
    if(message[i]>='a' and message[i]<='z'):
        plain_postion = alphabet_position[message[i]]
        key_char = repeatKey_positon[i]
        key_position = alphabet_position[key_char]
        pos=(key_position+plain_postion)
        cipher_text += position_alphabet[pos%26] 
    else :
        cipher_text +=' '    

print(f'the cipher text : {cipher_text}')

#for plain text
plain_text=''
for i in range(0,len(cipher_text)):
    if(cipher_text[i]>='a' and cipher_text[i]<='z'):
        plain_postion = alphabet_position[cipher_text[i]]
        key_char = repeatKey_positon[i]
        key_position = alphabet_position[key_char]
        pos=(plain_postion-key_position)
        if pos<0 : pos+=26
        plain_text += position_alphabet[(pos)%26] 
    else :
        plain_text+= ' '    

print(f'the plain text:{plain_text}')