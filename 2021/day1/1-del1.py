#! /usr/bin/env python3
import itertools

def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = itertools.tee(iterable)
    next(b, None)
    return zip(a, b)


def main():

    # Using readlines()
    file1 = open('input', 'r')
    Lines = file1.readlines()
    
    count = 0
    larger = 0

    for a, b in pairwise(Lines):
        if ( b > a ):
            larger += 1
    
    print(larger)


# Control execution of code
if __name__ == "__main__":
    main()