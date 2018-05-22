from random import randrange


def IsPrime(n):
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


def NOD(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return max(a, b)


def FindExp(phi):
    return e


def FindSecretExp(phi, e):
    for d in range(phi):
        if (d * e) % phi == 1:
            return d

command = input("Enter 's' to send the message, 'r' to recieve or 'k' to generate the key: ")
if command == 's':
    coms = input("Enter the public key: ").split()
    message = input("Enter the message: ")
    ord_letters = []
    for letter in message:
        ord_letters.append(ord(letter))
    new_text = ""
    for number in ord_letters:
        new_text += (str((number ** int(coms[0])) % int(coms[1])) + " ")
    print("Encrypted message: " + new_text)
elif command == 'r':
    coms = input("Enter your private key: ").split()
    message = input("Enter the message: ").split()
    int_message = []
    for i in message:
        int_message.append(int(i))
    new_text = ""
    for number in int_message:
        new_text += chr((number ** int(coms[0])) % int(coms[1]))
    print("Decrypted message: " + new_text)
elif command == 'k':
    p = 10
    q = 10
    while not IsPrime(p):
        p = randrange(500, 1000)
    while not IsPrime(q) or p == q:
        q = randrange(500, 1000)
    n = p * q
    phi = (p - 1) * (q - 1)
    e = randrange(2, phi)
    while NOD(e, phi) != 1:
        e = (e + 1)
    d = FindSecretExp(phi, e)
    print("Here is your SECRET key, do not tell it to anyone: " + str(d) + " " + str(n))
    print("Here is your PUBLIC key, send it to your friend: " + str(e) + " " + str(n))
else:
    print("Command not found!")
