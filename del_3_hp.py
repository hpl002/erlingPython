 #I stedenfor å drive å trikse med flere løkker så kan vi spare oss for litt arbeid. 
# Først kan vi se etter det som er felles:
    # Skal alltid starte og avslutte med 1 "x"
    # Øker og minsker med 2 "x" per linje
        # her må dere lage en formel
        # finnes sikkert en formlet på nettet et sted
    # figuren snur retning etter n linjer
    # lengden (altså antall) linjer er (n*2)-1


 

def print_x(n):    
    print('x' * n)

def print_diamond(N): # ikke endre den linjen
    print('Tall:', N)
    length  = (N*2)-1
    if int(length) > 0:      
        for i in range(int(length)):                  
            if i+1<N: #har ikke møtt midtpunktet enda, derav økning
                print("up")                 
            if i+1==N: #snur retning når vi har nådd midten av figuren. Husk index startet på 0 og ikke 1 derav i+1
                print("climax")                 
            if i+1>N: #har møtt midtpunktet derav nedtrapping
                print("down")


# ikke endre noe nedenfor
if __name__ == "__main__":
    print_diamond(25)
    print()
    
    print_diamond(2)
    print()
    
    print_diamond(3)
    print()
    
    print_diamond(4)
    print()
    
    print_diamond(10)
