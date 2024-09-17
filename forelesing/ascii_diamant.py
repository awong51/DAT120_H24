#size = int(input('write diamond size'))
def ascii_diamond(size):
    size -= 1
    print(' '*int(size) + '*')

    for i in range(size):
        print(' '*int(size-i-1) + '*' + ' '*int(i*2+1) + '*')

    for i in reversed(range(size-1)):
        print(' '*int(size-i-1) + '*' + ' '*int(i*2+1) + '*')

    print(' '*int(size) + '*')

ascii_diamond(5)

