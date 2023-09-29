red = "\033[0;31m"
cyan = "\033[0;36m"

# Original alphabet
alphabet = 'abcdefghijklmnopqrstuvw)xyz0123456789}{*(&^%$£"!-_=+[]:;@~#<,>.?/\|`¬ ZYXWVUTSRQPONMLKJIHGFEDCBA'

input_text = input(red + "Enter code to be encrypted: ")
numericalkey = input("Enter a positive whole number. This will be needed to decode the encrypted "
                     "message: ")

shifted_text = ""

for i in range(len(input_text)):
    shifted_text = shifted_text + alphabet[(alphabet.find(input_text[i]) + (int(numericalkey)*len(input_text)) + ((i**3)*int(numericalkey))) % len(alphabet)]

print("Original message:(" + cyan + str(input_text) + red + ")")
print("Encrypted message:(" + cyan + str(shifted_text) + red + ")")
print("Numerical key required to decode the message:(" + cyan + str(numericalkey) + red + ")")
