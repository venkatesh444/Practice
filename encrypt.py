from Crypto.Cipher import AES
AES.key=AES.new('This is a key')
message=input('Enter Text')
ciphertext= AES.key(message)
print(ciphertext)
