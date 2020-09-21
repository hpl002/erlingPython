# du kan definere flere hjelpefunksjoner om du trenger dem


def print_diamond(N): # ikke endre den linjen
    print('Tall:', N)
    if int(N) > 0:              
        for i in range(int(N)):
            for m in range (int(N) - i):    
                print(" ", end="")
            for j in range((i * 2) - 1):
                print("X", end="")
            print()
        for i in range(int(N), 0, -1):
            for m in range (int(N) - i):
                print(" ", end="")
            for j in range((i * 2) - 1):
                print("X", end="")
            print()      
    
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
