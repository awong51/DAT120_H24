
def funksjon(fil):
    linjenummer = 0
    resultat = {}
    with open(fil,encoding='utf-8') as file:
        for row in file:
            linjenummer += 1
            words = row.split()
            for word in words:
                if word in resultat:
                    continue
                else:    
                    resultat[word] = linjenummer
    return resultat
        


x = funksjon('DAT120 oving 1 intro til programmering.txt')

print(x)