def chiffrement_cesar(message, decalage):
    message_chiffre = ""
    for lettre in message:
        if lettre.isalpha():
            if lettre.isupper():
                message_chiffre += chr(((ord(lettre) - ord('A') + decalage) % 26) + ord('A'))
            else:
                message_chiffre += chr(((ord(lettre) - ord('a') + decalage) % 26) + ord('a'))
        else:
            message_chiffre += lettre
    return message_chiffre

message_original = "Hello, Caesar!"
decalage = 3
message_chiffre = chiffrement_cesar(message_original, decalage)
print("Message original:", message_original)
print("Message chiffré:", message_chiffre)

