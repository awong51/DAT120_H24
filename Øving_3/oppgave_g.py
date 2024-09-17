def kinetisk_energi(m,v):
    return (f'{0.5*m*(v**2)} m/s')

masse = int(input('Hva er massen?\n'))
fart = int(input('Hva er farten?\n'))

print(kinetisk_energi(masse,fart))
    