import math

prime_p = int(input('enter the prime p : '))
prime_q = int(input('enter the prime q : '))

n = prime_p * prime_q
phi_n = (prime_p-1) * (prime_q-1)


print('the number of possible value of e: ')
for e in range(2,phi_n):
    if(math.gcd(e,phi_n)==1):
        print(e, end=' ')
print(' ')

e = int(input('enter a value of e: '))
assert e<n, 'error'

for d in range(2,phi_n):
    if (d*e) % phi_n == 1 :
        break

print(f'public key: {e} ,{n}')
print(f'decrypted key:{d}, {n}')

message = int(input('enter the message: '))
encrypted_message = pow(message,e,26)
decrypted_message = pow(encrypted_message,d)%26 
print(f'encrypted message : {encrypted_message}')
print(f'decrypted message ; {decrypted_message}')