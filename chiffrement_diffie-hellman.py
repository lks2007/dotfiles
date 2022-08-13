import Crypto.Util.number as cun
from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES
import hashlib
import secrets

BLOCK_SIZE = 32

def generate_keys(person,secret):
    privatekey = secrets.randbelow(100000000000000000000000000000000000000000000000000000000000000000000000000)

    with open((str("{0}_privatekey").format(person)), "w") as f:
        f.write(str(privatekey))
        f.close()

    with open((str("{0}_publickey").format(person)), "w") as f:
        f.write(str(secret^privatekey))
        f.close()

def read_keys(person,keytype):
    with open(str("{0}_{1}key").format(person,keytype)) as f:
        key_person = f.read()
        f.close()

    return key_person
        
def encrypt(msg, publickey_receiver, privatekey_sender):
    secret = int(publickey_receiver)^int(privatekey_sender)

    key = hashlib.sha256(cun.long_to_bytes(secret)).digest()[:16]
    cipher = AES.new(key, AES.MODE_ECB)
    
    cipherText = cipher.encrypt(pad(bytes(msg, "utf-8"), BLOCK_SIZE))
    cipherFlag = cipherText.hex()

    return cipherText, cipherFlag

def decrypt(msg, publickey_sender , privatekey_receiver):
    secret = int(publickey_sender)^int(privatekey_receiver)

    key = hashlib.sha256(cun.long_to_bytes(secret)).digest()[:16]
    cipherText = bytes.fromhex(cipherFlag)
    cipher = AES.new(key, AES.MODE_ECB)
    plaintext = cipher.decrypt(cipherText)
    
    return plaintext.decode('utf-8')


if __name__ == '__main__':

    sender="romeo"
    receiver="juliette"
    
    keytypes = ["private","public"]
    persons=[sender,receiver]    
    
    msg=input("Entrer votre message: ")

    print("message: {}".format(msg))
    
    secret = secrets.randbelow(10000000000000000000000000000)
    
    for person in persons:
        generate_keys(person,secret)
         
    for keytype in keytypes:
        if keytype == "public":
            publickey_sender = read_keys(sender,keytype)
            publickey_receiver = read_keys(receiver,keytype)
        elif keytype == "private":
            privatekey_sender = read_keys(sender,keytype)
            privatekey_receiver = read_keys(receiver,keytype)
        
    cipherText, cipherFlag = encrypt(msg, publickey_receiver, privatekey_sender)
    print("Message chiffré: {}".format(cipherText.hex()))
    
    sub_string = "\x1a"
    plainText = decrypt(msg, publickey_sender, privatekey_receiver).replace(sub_string, "")

    print("Message déchiffré: {}".format(plainText))
