print("Welcme to the world of cryptography")

def main():
    print()
    print("Choose one option")
    choice = int(input("1. Encryption\n2. Decryption\nChoose(1,2): "))
    if choice == 1:
        encryption()
    elif choice == 2:
        decryption()
    else:
        print("Wrong Choice")


def encryption():
    print("Encryption")
    msg = input("Enter your message: ")
    key = int(input("Enter key (1-94): "))
    encrypted_text = ""
    for i in range(len(msg)):
        temp = (ord(msg[i]) + key)
        if (temp > 126):
            temp = temp - 127 + 32

        encrypted_text += chr(temp)
    print("Encrypted: " + encrypted_text)

def decryption():
    print("Decryption")
    print("Message can only be lower or upper alphabet!")
    encrypt_msg = input("Enter encrypted text: ")
    decrypt_key = int(input("Enter key (1-94): "))
    decrypted_text = ""
    for i in range(len(encrypt_msg)):
        temp = (ord(encrypt_msg[i]) - decrypt_key)
        if (temp > 126):
            temp = temp + 127 - 32

        decrypted_text += chr(temp)
    print("Decrypted: " + decrypted_text)

if __name__ == "__main__":
    main()
