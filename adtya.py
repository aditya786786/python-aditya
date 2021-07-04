import hashlib

crypt=hashlib.md5 ()
crypt.update (b"hello")

print (crypt.hexdigest())
print (crypt.digest_size)
