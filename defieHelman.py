import math

prime_q = int(input('enter a prime number q: '))

def generate_primitive_root(num, prime_q):
    co_prime1 = {val for val in range(1,prime_q)}
    co_prime2=set({})
    for p in range(0,prime_q):
        co_prime2.add(pow(num,p,prime_q))
    return co_prime1 == co_prime2






   

for val in range(1,prime_q):
    if generate_primitive_root(val,prime_q) :
        print(val,end=' ')
print('')

primitive_root=int(input('select a primitve root: '))
xa =int(input('A user private key: '))
assert xa < prime_q, "Error" #secret key prime thake soto hote hobe
xb = int( input('B user private key: '))
assert xb < prime_q, "Error"

user_A_public_key = pow(primitive_root, xa) % prime_q
user_B_public_key = pow(primitive_root, xb, prime_q)

print(user_A_public_key, user_B_public_key)

user_A_secret_key = pow(user_B_public_key,xa,prime_q)
user_B_secret_key = pow(user_A_public_key,xb,prime_q)
print(f'user A secret key: {user_A_secret_key}')
print(f'user B secret key: {user_B_secret_key}')
