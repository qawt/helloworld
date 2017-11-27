print("This prints out a X-pattern in n by n size,");
print("and supports multi character patterns.")

n = int(input("How big do you want this? (positive int) "))

if n < 1:
    raise ValueError("bad n")

c = input("What letters do you want to use? ")

spaceSize = len(c)

def printX(n, c):
    for i in range(0, n):
        for j in range(0, n):
            if i == j or i == (n-1)-j:
                print(c, end='')
            else:
                print(' '*spaceSize, end='')
        print('')

printX(n, c)

print('\nwhat do you think? :)')
