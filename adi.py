import hashlib
def main():
    text= "hello world!"
    textUtf8= text.encode("utf-8")

    hash= hashlib.md5 ( textUtf8 )
    hexa= hash.hexdigest()
    print(hexa)

    return
main()
