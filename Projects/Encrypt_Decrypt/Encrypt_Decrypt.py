import base64
import os

password = input("Enter your password :- ")
encode_password = password.encode("ascii")  # The encode method converts the string into bytes in ASCII encoding
base64_bytes = base64.b64encode(encode_password)  # It returns a bytes object containing the Base64-encoded password
encrypt = base64_bytes.decode("ascii")  # Base64-encoded password bytes object is converted back to a string.
print("The Encrypted password :- " + encrypt)

decode_password = encrypt.encode("ascii")  # The encode method converts the string into bytes in ASCII encoding
base64_bytes = base64.b64decode(decode_password)  # It decodes Base64-encoded password back to original form as bytes
decrypt = base64_bytes.decode("ascii")  # Bytes object with the "ascii" converted back to a string.
print("The Decrypted password :- " + decrypt)
