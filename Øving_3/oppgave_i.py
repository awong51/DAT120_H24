def euklidske_avstanden(x,y):
    ans = (x**2+y**2)**(1/2)
    return ans

punkt_a = input('Hva er punkt a? (skriv med komma mellom x og y, eks. 1,4)')
punkt_b = input('Hva er punkt b? (skriv med komma mellom x og y, eks. 1,4)')

x1,y1 = map(float, punkt_a.split(','))
x2,y2 = map(float, punkt_b.split(','))

delta_x = x2 - x1
delta_y = y2 - y1

print(delta_x,delta_y)
print(euklidske_avstanden(delta_x,delta_y))