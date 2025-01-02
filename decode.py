def encrypt(word):
    prefix="axt"
    suffix="lqz"
    if len(word)<3:
        return word[::-1]
    modified=word[1:]+word[0].lower()
    return prefix + modified + suffix
        

def decrypt(word):
    prefix="axt"
    suffix="lqz"
    if len(word)<3:
        return word[::-1]
    modified=word[len(prefix):-len(suffix)]
    return modified[-1]+modified[:-1]
        
ans=str(input("Enter if you want to Code or Decode: ")).lower()

if ans=="code":
    word=str(input("Enter the word you want to encrypt: ")).strip()
    if word:
        encrypted_word=encrypt(word)
        print(f"Your encrypted word is: {encrypted_word}")
    else:
        print("Word can not be empty!")

elif ans=="decode":
    word=str(input("Enter the word you want to decrypt: ")).strip()
    if word:
        decrypted_word=decrypt(word)
        print(f"Your decrypted word is: {decrypted_word}")
    else:
        print("Word can not be empty!")
else:
    print('Invalid option! Please choose "code" or "decode" ')

print("\nThank you for using this program!")