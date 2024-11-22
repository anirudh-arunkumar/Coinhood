import nacl.signing
import base64

private_key = nacl.signing.SigningKey.generate()
public_key = private_key.verify_key

private_key_base64 = base64.b64encode(private_key.encode()).decode()
public_key_base64 = base64.b64encode(public_key.encode()).decode()

print("Private Key (Base64):", private_key_base64)
print("Public Key (Base64):", public_key_base64)
