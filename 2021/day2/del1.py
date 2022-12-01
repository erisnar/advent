#! /usr/bin/env python3

def main():
    horizontal = 0
    depth = 0
    aim = 0

    with open('input') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]
        for line in lines:
            command, value = line.split()
            match command:
                case "forward":
                    horizontal += int(value)
                case "down":
                    depth += int(value)
                case "up":
                    depth -= int(value)
                case _:
                    print("Code not found")
    
    print("horizontal: ", horizontal)
    print("depth: ", depth)
    sum = horizontal * depth
    print("sum: ", sum)
            
# Control execution of code
if __name__ == "__main__":
    main()