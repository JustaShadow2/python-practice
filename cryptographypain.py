'''(Alphabet Number * key)mod(total number of alphabets)'''
def encrypt():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'

    string1 = input('input: ')
    string2 = string1.lower()

    key1 = int(756) #you can change these up to change the encrypted letters, bigger = harder to brute force
    key2 = int(11)

    ciphertext = ('')

    for i in string2:
        letter = alphabet.find(i)
        newletter = ((letter*key1)+key2)%26
        ciphertext += alphabet[newletter]

    print(ciphertext)

encrypt()


#biggest drawback, letters that are the same will also be the same
#after encryption. Now that fundamentals work need to make a new 
#mathematical process