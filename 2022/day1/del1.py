#! /usr/bin/env python3

def main():

    # Using readlines()
    file = open('input', 'r')
    Lines = file.readlines()
    newElf = False
    elfs = [0] * len(Lines)
    i = 0
    
    for calories in Lines:
        if "\n" == calories:
            newElf = True
        
        if newElf == True:
            i += 1
            newElf = False
        else:
            elfs[i] += int(calories)
            
    print(max(elfs))

# Control execution of code
if __name__ == "__main__":
    main()