from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
import getpass

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

# Prompt the user for a password to encrypt the private key
password = getpass.getpass("Enter a password to encrypt the private key: ")

# Saving encrypted private key
encrypted_pem_private_key = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.BestAvailableEncryption(password.encode())
)
with open("private_key.pem", "wb") as f:
    f.write(encrypted_pem_private_key)

# Saving public key
pem_public_key = private_key.public_key().public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)
with open("public_key.pem", "wb") as f:
    f.write(pem_public_key)
