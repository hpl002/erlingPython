
#kommentar: dette fungerer helt fint, men her vil jeg være stødig på hvilke versjon av python dere kjører. 
# Tror ikke template literals fungerer i python 2.x.x

import sys
print(sys.version) #Her skriver jeg ut hvilke versjon fu kjører på. Har foreleser spesifisert en versjon? Det er stor forskjell fra versjon 3.x.x til 2.x.x


 


# du kan definere flere hjelpefunksjoner om du trenger dem


def complement(dna_in): # ikke endre den linjen
    
    out = ''
    for letter in dna_in:
        if letter == 'T':
            out += 'A'
            continue
        if letter == 'A':
            out += 'T'
            continue
        if letter == 'G':
            out += 'C'
            continue
        if letter == 'C':
            out += 'G'
            continue
        
    return out [::-1]
    
    
# ikke endre noe nedenfor
if __name__ == "__main__":
    in_1 = "ATAGCAGT"
    out_1 = complement(in_1)
    
    print(f"The complement of {in_1} is {out_1}") #denne vil ikke fungere i python 2 (i det minste den versjonen jeg hadde --> Python 2.7.16 ). Hør evt med foreleser om hvilke versjon dere skal kjøre. 
    if out_1 == "ACTGCTAT":
        print('That is correct!')

    check = complement(complement(in_1))
    if in_1 == check:
        print('Good! Applying complement twice returns the original')
    else:
        print('Hmm. This does not work.')



#PYTHON 2
#❯ python del_1.py
#  File "del_1.py", line 2
#SyntaxError: Non-ASCII character '\xc3' in file del_1.py on line 2, but no encoding declared; see http://python.org/dev/peps/pep-0263/ for details

#PYTHON 3
#❯ python3 del_1.py
#The complement of ATAGCAGT is ACTGCTAT
#That is correct!
#Good! Applying complement twice returns the original
 