# There is currently an issue with the numeric key in that it provides little to no security,
# due to encryption machine working on a base 96 system which is the length of "alphabet".
# I will try and make the key system more useful in a later version.
# Potential idea may be to construct "alphabet" This would certainly resolve the issue of an insufficient
# amount of settings (96! to be precise)
# possibly fixed. Just need to check derangement gives a sufficient amount of derangement's
# If fixed then will try and add output length changes
# Take a running score for alphabet of input code to modify numericalkey (this will be hard to decode)
# More experimentation needed for derangement make. It is not giving 96! derangement's
# alphabet permutes all 96! combinations now. Next step is to add in feature that scrambles same length
# sentences with similar structures (e.g "hello sir" and "hello sit" give similar encryption's)

import math

red = "\033[0;31m"
cyan = "\033[0;36m"

# Original alphabet
alphabet = 'abcdefghijklmnopqrstuvw)xyz0123456789}{*(&^%$£"!-_=+[]:;@~#<,>.?/\|`¬ ZYXWVUTSRQPONMLKJIHGFEDCBA'

input_text = input(red + "Enter encrypted message: ")
numerical_key = input("Enter the secret positive whole number given to you by the sender of the message: ")
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
    shifted_text = shifted_text + new_alphabet[
        (new_alphabet.find(input_text[i]) - (int(numerical_key_store) * len(input_text)) - (
                (i ** 3) * int(numerical_key_store))) % len(
            new_alphabet)]

print("Encrypted message:(" + cyan + str(input_text) + red + ")")
print("Numerical key used:(" + cyan + str(numerical_key_store) + red + ")")
print("Decrypted message:(" + cyan + str(shifted_text) + red + ")")
