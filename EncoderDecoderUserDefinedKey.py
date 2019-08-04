# EncoderDecoderUserDefinedKey.py
# Billy Ridgeway
# Encode or decode your messages by shifting the ASCII characters by an amount defined by the user.

output = ""                                                 # Sets the output string to an empty string.
message = input("Enter a message to encode or decode: ")    # Prompt the user for a message to encode/decode.
message = message.upper()                                   # Convert the string of letters to upper case.
inOut = ""                                                  # Sets the inOut string to an empty string.

# Ask the user to create a key to encode or decode the message. The key must be a number between 1 and 26.
userKey = int(input("Enter a number between 1 and 26 to be used as your encoding/decoding key: "))

while userKey < 1 or userKey > 26:                                          # Checks to ensure that the user entered a valid number for thier key.
    userKey = int(input("Please enter a number between 1 and 26: "))    

inOut = input("Please enter 'e' to encode or 'd' to decode: ").upper()      # Prompts the user to select encoding or decoding of their message.

if (inOut != 'E' and inOut != 'D'):                                         # Checks to ensure that the user entered a valid selection.
    inOut = input("Please enter 'e' to encode or 'd' to decode: ").upper()

if inOut == 'E':                                                # A loop to encode each letter in the message.                                
    for letter in message:                                      
        if letter.isupper():                                    # Checks to see if the letter is already in upper case.
            value = ord(letter) + userKey                       # Converts the letter to it's corresponding ASCII number and adds the key input by the user..
            letter = chr(value)                                 # Converts an ASCII number to a letter.
            if not letter.isupper():                            # This loop runs to ensure that the ASCII number hasn't shifted too far and gone past 'Z'.
                value -= 26                                     # This subtracts 26 from the number to ensure it's in the range from 'A' to 'Z'.
                letter = chr(value)                             # Converts the ASCII value to a letter.
        output += letter                                        # Add the letter to the output string.
        
elif inOut == 'D':                                              # A loop to decode each letter in the message.
    for letter in message:                                     
        if letter.isupper():                                    # Checks to see if the letter is already in upper case.
            value = ord(letter) - userKey                       # Converts the letter to it's corresponding ASCII number using the user's key.
            letter = chr(value)                                 # Converts an ASCII number to a letter.
            if not letter.isupper():                            # This loop runs to ensure that the ASCII number hasn't shifted too far and gone past 'Z'.
                value += 26                                     # This adds 26 from the number to ensure it's in the range from 'A' to 'Z'.
                letter = chr(value)                             # Converts the ASCII value to a letter.
        output += letter                                        # Add the letter to the output string.
    
print("Output message: ", output)                               # Prints the encoded/decoded message to the screen.


