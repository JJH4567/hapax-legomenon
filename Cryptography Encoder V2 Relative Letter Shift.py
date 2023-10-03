import math

red = "\033[0;31m"
cyan = "\033[0;36m"

# Original alphabet
alphabet = 'abcdefghijklmnopqrstuvw)xyz0123456789}{*(&^%$£"!-_=+[]:;@~#<,>.?/\|`¬ ZYXWVUTSRQPONMLKJIHGFEDCBA'

input_text = input(red + "Enter code to be encrypted: ")
numerical_key = input("Enter a positive whole number. This will be needed to decode the encrypted "
                      "message: ")
numerical_key_store = numerical_key

new_alphabet = ""
store = ""
counter = len(alphabet)

while counter > 0:
    new_alphabet = new_alphabet + alphabet[divmod(int(numerical_key), math.factorial(counter - 1))[0]]
    store = alphabet[divmod(int(numerical_key), math.factorial(counter - 1))[0]]
    numerical_key = divmod(int(numerical_key), math.factorial(counter - 1))[1]
    alphabet = alphabet.replace(store, "")
    counter = counter - 1

shifted_text = ""

for i in range(len(input_text)):
    shifted_text = shifted_text + new_alphabet[(new_alphabet.find(input_text[i]) + (
                int(numerical_key_store) * len(input_text)) + ((i ** 3) * int(numerical_key_store))) % len(
        new_alphabet)]

print("Original message:(" + cyan + str(input_text) + red + ")")
print("Encrypted message:(" + cyan + str(shifted_text) + red + ")")
print("Numerical key required to decode the message:(" + cyan + str(numerical_key_store) + red + ")")
