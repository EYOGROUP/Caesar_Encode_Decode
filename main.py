alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def Caeser (get_text, get_schift,get_direction):
    end_text_as_string = ''
    
    if direction == "decode":
        get_schift *= -1
        
    for letter in get_text:
        if letter not in alphabet:
            end_text_as_string += letter
            
            
        else:
                
             position = alphabet.index(letter)
             new_position = position + get_schift
             end_text_as_string += alphabet[new_position]
             
    print(f"you message from {get_direction} is {end_text_as_string}")
        
from logo import logo

print(logo)    
    
stop_the_process = True
while stop_the_process:
        
        direction = input("if you want to encode your Message Typ 'encode', otherweise if you want to decode your Message Type 'decode': ")

        text = input("Enter your text that you want to encode or decode: ").lower()
        shift = int(input("Enter the shift number ")) 
        
        Caeser(get_text= text, get_schift=shift,get_direction=direction)   

        question = input("Typ 'yes' if you want to do again. Otherweis type 'no'") 
        if direction == "no":
            stop_the_process = False
          
        else: 
            stop_the_process = True
