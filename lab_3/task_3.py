def encrypt():
    char=input("enter your word")
    num=int(input("enter your shift number"))
    for ch in char:
        e=""
        new=(chr((ord(ch)-ord('a')+num%26)+ord('a')))
        print(new)
encrypt()
def decrypt():
    char=input("enter your word")
    num=int(input("enter your shift number"))
    for ch in char:
        e=""
        new=(chr((ord(ch)-ord('a')-num%26)+ord('a')))
        print(new)
decrypt()