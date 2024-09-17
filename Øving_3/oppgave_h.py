def euklidske_avstanden(x,y):
    ans = (x**2+y**2)**(1/2)
    return ans

x = int(input('x verdi?'))
y = int(input('y verdi?'))

print(euklidske_avstanden(x,y))