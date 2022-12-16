letters = "abcdefghijklmnopqrstuvwxyz"
message = open('messagetwo.txt', 'r')
messageDecryption = message.read()
x = 0
while x < 26:
    x = x + 1 
    decryptionString= messageDecryption
    decryptionString= decryptionString.lower()
    cipher=int(x)
    messageDecrypted=""
    for character in decryptionString:
        position = letters.find(character)
        newposition = position - cipher
        if character in letters:
            messageDecrypted = messageDecrypted + letters[newposition]
        else:
            messageDecrypted = messageDecrypted + character
            
    cipher=str(cipher)
    print("You used a cipher shift of "+cipher)
    print("=-=-=-=-=-=-=-=-=-=")
    print("Your decrypted message reads:")
    print(messageDecrypted)
    print("\n")
    print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")