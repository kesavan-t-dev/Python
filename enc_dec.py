"""
encryption and decryption using three libraries
"""

#-----------------------#
#  fernet cryptography  #
#-----------------------#
# Fernet module 
from cryptography.fernet import Fernet

# key is generated
key = Fernet.generate_key()
print("key value:",key)
# value of key is assigned to a variable
f = Fernet(key)
print("f value:",f)
# the plaintext is converted to ciphertext
token = f.encrypt(b"welcome to geeksforgeeks")

# display the ciphertext
print("token value after encrypt:",token)

# decrypting the ciphertext
d = f.decrypt(token)

# display the plaintext
print(d.decode())


"""

#-----------------------#
#  AES cryptography     #
#-----------------------#

from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()
cipher = Fernet(key)

# Encrypt
text = b"abcde"
print("byte code values are",list(text))
text = "Encryption"
encrypted = cipher.encrypt(text.encode())


# Decrypt
decrypted = cipher.decrypt(encrypted).decode()

print("Key:", key)
print("Encrypted:", encrypted)
print("Decrypted:", decrypted)"""

