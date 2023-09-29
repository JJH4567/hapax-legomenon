red = "\033[0;31m"
cyan = "\033[0;36m"

# Original alphabet
alphabet = 'abcdefghijklmnopqrstuvw)xyz0123456789}{*(&^%$£"!-_=+[]:;@~#<,>.?/\|`¬ ZYXWVUTSRQPONMLKJIHGFEDCBA'

input_text = input(red + "Enter encrypted message: ")
numericalkey = input("Enter the secret positive whole number given to you by the sender of the message: ")

shifted_text = ""

for i in range(len(input_text)):
    shifted_text = shifted_text + alphabet[
        (alphabet.find(input_text[i]) - (int(numericalkey) * len(input_text)) - ((i ** 3) * int(numericalkey))) % len(
            alphabet)]

print("Encrypted message:(" + cyan + str(input_text) + red + ")")
print("Numerical key used:(" + cyan + str(numericalkey) + red + ")")
print("Decrypted message:(" + cyan + str(shifted_text) + red + ")")
