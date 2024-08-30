import string
import argparse


def cesar(w, d):
    palabra_enc = ""
    for i in w:
        if i.isalpha():
            offset = 65 if i.isupper() else 97
            letra_enc = chr((ord(i) - offset + d)%26 + offset)
            palabra_enc += letra_enc
        else:
            palabra_enc += i 

    return(palabra_enc)

parser = argparse.ArgumentParser()

parser.add_argument("Palabra", type=str)
parser.add_argument("Desp", type=int)

args = parser.parse_args()

palabra_enc = cesar(args.Palabra, args.Desp)
print(palabra_enc)  

