'''printx'''

def do_print_x(size, character):
    '''print c char in nxn pattern'''
    space_size = len(character)

    for i in range(0, size):
        for j in range(0, size):
            if i == j or i == (size-1)-j:
                print(character, end='')
            else:
                print(' '*space_size, end='')
        print('')

def main():
    '''Main execution program'''
    print("This prints out a X-pattern in n by n size,")
    print("and supports multi character patterns.")
    n_input = int(input("How big do you want this? (positive int) "))
    c_input = input("What letters do you want to use? ")

    if n_input < 1:
        raise ValueError("bad n")

    do_print_x(n_input, c_input)

    print('\nwhat do you think? :)')

if __name__ == "__main__":
    main()
