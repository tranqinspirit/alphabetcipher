# simple substitution cipher of sorts
import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

max_length = len(alphabet) - 1

def cipher(word, step):
    cipher = word
    counter = 0
    for x in cipher:
        if x != ' ':
            index = alphabet.index(cipher[counter])
            
            check = -1
       
            if (index + step >= max_length):
                check = ((index + step) - index)
                check = check - 1
            else:
                check = index + step
           
            cipher[counter] = alphabet[check]
            
        counter = counter + 1
    
    return cipher

def convertlisttostring(s):
    new = ""

    for x in s:
        new  += x
    return new

def main():
    loop = True
    while loop:
        step_max = int(input("Enter max number of steps: "))
        word = input("Enter message: ")
        step = random.randrange(1,step_max,1)

        word = word.lower()
        word = list(word)
        new_word = cipher(word, step)
        new_word = convertlisttostring(new_word)
        print(str(step) + ' ' + new_word)

if __name__ == "__main__":
    main()
