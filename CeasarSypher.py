logo = """           
 ,adPPYba,  ,adPPYYba,   ,adPPYba,  ,adPPYba,  ,adPPYYba,  8b,dPPYba,  
a8"     ""  ""     `Y8  a8P_____88  I8[    ""  ""     `Y8  88P'   "Y8  
8b          ,adPPPPP88  8PP'''''''   `"Y8ba,   ,adPPPPP88  88          
"8a,   ,aa  88,    ,88  "8b,   ,aa  aa    ]8I  88,    ,88  88          
 `"Ybbd8"'  `"8bbdP"Y8   `"Ybbd8"'  `"YbbdP"'  `"8bbdP"Y8  88   

                          88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP''''''' 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
is_over = False


def encrypt(t, s, fb):
  code = ""
  if fb == True:
    for letter in t:
      if letter in alphabet:
        letter_index = alphabet.index(letter)
        code += alphabet[letter_index + s]
      else:
        code += letter
  else:
    for letter in t:
      if letter in alphabet:
        letter_index = alphabet.index(letter)
        code += alphabet[letter_index - s]
      else:
        code += letter
  print(f"Your crypted code is: {code}")


def decrypt(t, s, fb):
  code = ""
  if fb == True:
    for letter in t:
      if letter in alphabet:
        letter_index = alphabet.index(letter)
        code += alphabet[letter_index - s]
      else:
        code += letter
  else:
    for letter in t:
      if letter in alphabet:
        letter_index = alphabet.index(letter)
        code += alphabet[letter_index + s]
      else:
        code += letter
  print(f"Your decrypted code is: {code}")


while is_over != True:
  print(logo)
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  if direction != "encode" and direction != "decode":
    print("Wrong input try again")
  else:
    t = input("Type your message:\n").lower()
    s = int(input("Type the shift number:\n"))
    fb = int(input("What type of shift?\nBack (0) or forward (1):\n"))
    if direction == "encode": 
      encrypt(t,s,fb)
    if direction == "decode":
      decrypt(t,s,fb)
  
  end_game = input("Do you want to end Cesar Cypher encryption?\nYes or No?\n")
  if end_game == "Yes":
    is_over = True
