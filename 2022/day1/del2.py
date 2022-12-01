#! /usr/bin/env python3

def main():

    # Using readlines()
    file = open('input2', 'r')
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

    elfs.sort()
    
    print("Top 3:", (elfs[-1]+elfs[-2]+elfs[-3]))

# Control execution of code
if __name__ == "__main__":
    main()