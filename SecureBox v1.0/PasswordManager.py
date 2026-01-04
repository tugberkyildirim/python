import random
import base64
import os
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

RSA_DIR = "Data/RSA/"

symbols_list = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '"', '!', "'", '^', '+', '%', '&', '/', '(', ')', '=', '?', '_', 
    '*', '-', '<', '>', '£', '#', '$', '½', '{', '[', ']', '}', '\\', '|', '@', '~', '€', '.', ',', ';', ':'
]

def create_random_password(isNumeric, isSymbol, isBigChar, isLowChar, password_length):
    low_chars = "abcdefghijklmnopqrstuvwxyz"
    big_chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    digits = "0123456789"
    special_symbols = "".join([char for char in symbols_list if not char.isalnum()])

    pool = ""
    if isLowChar: pool += low_chars
    if isBigChar: pool += big_chars
    if isNumeric: pool += digits
    if isSymbol: pool += special_symbols

    if not pool:
        return "Hata: En az bir karakter tipi seçmelisin!"

    generated_password = "".join(random.choice(pool) for _ in range(password_length))
    
    return generated_password

def encode_base64(data):return base64.b64encode(data.encode("utf-8")).decode("ascii")
def decode_base64(data):return base64.b64decode(data).decode("utf-8")

def generate_rsa_keys(key_size):
    key = RSA.generate(key_size)
    private_key = key.export_key().decode()
    public_key = key.publickey().export_key().decode()
    return private_key, public_key

def rsa_encrypt(message, public_key):
    recipient_key = RSA.import_key(public_key)
    cipher_rsa = PKCS1_OAEP.new(recipient_key)
    enc_data = cipher_rsa.encrypt(message.encode("utf-8"))
    return base64.b64encode(enc_data).decode("ascii")

def rsa_decrypt(enc_data, private_key):
    code = RSA.import_key(private_key)
    cipher_rsa = PKCS1_OAEP.new(code)
    dec_data = cipher_rsa.decrypt(base64.b64decode(enc_data))
    return dec_data.decode("utf-8")

def generate_rsa_keys(key_size):
    key = RSA.generate(key_size)
    private_key = key.export_key().decode()
    public_key = key.publickey().export_key().decode()
    return private_key, public_key

def save_rsa_to_disk(priv, pub):
    if not os.path.exists(RSA_DIR):
        os.makedirs(RSA_DIR)
    with open(os.path.join(RSA_DIR, "private.pem"), "w") as f:
        f.write(priv)
    with open(os.path.join(RSA_DIR, "public.pem"), "w") as f:
        f.write(pub)

def load_rsa_from_disk():
    priv_path = os.path.join(RSA_DIR, "private.pem")
    pub_path = os.path.join(RSA_DIR, "public.pem")
    
    if os.path.exists(priv_path) and os.path.exists(pub_path):
        with open(priv_path, "r") as f:
            priv = f.read()
        with open(pub_path, "r") as f:
            pub = f.read()
        return priv, pub
    return None, None