'''Programming Set 2

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    #library
    alpha_shift=shift%26
    cap_letter=letter.upper()
    alpha_index=ord(cap_letter)
    alpha_index_new=alpha_index+shift
    new_letter=chr((alpha_index-ord("A")+alpha_shift)%26+ord("A"))
    #CONDITIONS
    #condition if the letter is a space
    if letter==' ':
        return letter
    #character is a letter in the alphabet
    if cap_letter.isalpha()==True:
        return new_letter
    print("Please enter a letter.")

letter="z"
shift=81
shift_letter(letter,shift)

def caesar_cipher(message, shift):
    '''Caesar Cipher.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    result=[]
    for char in message:
        char_index=ord(char)
        char_shift=shift%26
        new_char=chr((char_index-ord("A")+char_shift)%26+ord("A"))
        if char==' ':
            result.append(char)
        elif char.isalpha():
            result.append(new_char.upper())
    return ''.join(result)
message="hilu"
shift=100
caesar_cipher(message, shift)

def shift_by_letter(letter, letter_shift):
    #THOUGHT DUMP
    #shift=A->65-ord("A")
    #shift=B->66-ord("A")
    #shift=(ord(letter_shift.upper())-ord("A"))
    #new_letter=shift+ord(letter.upper())
    #if letter==' ': -> return letter
    '''Shift By Letter.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if letter==' ':
        return letter
    elif letter.isalpha() and letter_shift.isalpha():
        letter_cap=letter.upper()
        letter_shift_cap=letter_shift.upper()
        shift=ord(letter_shift_cap)-ord("A")
        new_letter=chr((shift+ord(letter_cap)-ord("A"))%26+ord("A"))
        return new_letter
letter="h"
letter_shift="k"
shift_by_letter(letter, letter_shift)
        

def vigenere_cipher(message, key):
    '''Vigenere Cipher.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A" -> make KEY equal to the length of the message

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

Set numerical equivalent of K, E, and Y -> transverse shifting through the letters -> shift the 
corresponding letters of the message according to the ord of K, E, and Y
    
    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    result=[]
    #ensure that length of key is longer than length of message, then slice [:len(message)] key to match 
    #length of msg
    key_upgrade=(key.strip()*(len(message)//len(key.strip())+1))[:len(message)] 
    #in list form, pairs the characters in the message and the key
    for char, letter in zip(message,key_upgrade):
            char=char.upper()
            letter=letter.upper()
            shift=ord(letter)-ord("A")
            char_index=ord(char)
            char_shift=shift%26
            new_char=chr((char_index-ord("A")+char_shift)%26+ord("A"))
            #simply returns spaces in the message as is
            if char==' ':
                result.append(char)
            #the actual writing of the new message
            elif char.isalpha():
                result.append(new_char.upper())
    return ''.join(result)
message="hilu"
key="key"
vigenere_cipher(message, key)



def scytale_cipher(message, shift):
    '''Scytale Cipher.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    result=['']
    length=len(message.upper().strip())
    remainder=length%shift
    if remainder !=0:
        message=message.upper().strip()+"_"*(shift-remainder)
    encrypted_message=result*len(message)
    for i in range(len(message)): 
        index=(i // shift) + (len(message) // shift) * (i % shift)
        encrypted_message[i]=message[index]
        
    return ''.join(encrypted_message)
message="INFORMATION_AGE"
shift=4
scytale_cipher(message,shift)



def scytale_decipher(message, shift):
    '''Scytale De-cipher.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    result=['']
    length=len(message.upper().strip())
    decrypted_message=result*length
    for i in range(len(message)):
        shift_rows=length//shift
        index=(i % shift_rows) * shift + (i // shift_rows)
        decrypted_message[i]=message[index]
    return ''.join(decrypted_message)

message="IRIANMOGFANEOT__"
shift=4
scytale_decipher(message, shift)