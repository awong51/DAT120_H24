import matplotlib.pyplot as plt


class Maalinger_aar:
    def __init__(self, aar):
        self.aar = aar
        self.total_solflekker = 0
        self.antall_maalinger = 0
        self.maks_daglig = 0
        self.min_daglig = 1000000

    def ny_maaling(self, antall_solflekker):
        self.total_solflekker += antall_solflekker
        self.antall_maalinger += 1

        if self.maks_daglig < antall_solflekker:
            self.maks_daglig = antall_solflekker
        
        if self.min_daglig > antall_solflekker and self.min_daglig != 0:
            self.min_daglig = antall_solflekker

    def gjennomsnitt(self):
        return self.total_solflekker / self.antall_maalinger
        
if __name__ == "__main__":
    aarlig_maaling = {}
    with open('solflekkaktivitet_daglig.csv', encoding='utf-8') as fil:
        for linje in fil:
            data = linje.strip().split(';')
            aar = int(data[0])
            antall_solflekker = int(data[4])

            if antall_solflekker == -1:
                continue

            if aar not in aarlig_maaling:
                aarlig_maaling[aar] = Maalinger_aar(aar)
            
            aarlig_maaling[aar].ny_maaling(antall_solflekker)

    x_aksen = []
    gjennomsnitt_graf = []
    maks_graf = []
    min_graf = []

    for aar in aarlig_maaling:
        x_aksen.append(aar)
        gjennomsnitt_graf.append(aarlig_maaling[aar].gjennomsnitt())
        maks_graf.append(aarlig_maaling[aar].maks_daglig)
        min_graf.append(aarlig_maaling[aar].min_daglig)
    
    plt.title("Solflekkaktivitet hvert år")
    plt.plot(x_aksen, gjennomsnitt_graf, color = 'black', label = "Gjennomsnitt")
    plt.plot(x_aksen, maks_graf, color = 'red', linestyle='dashed', label = "Maksimum")
    plt.plot(x_aksen, min_graf, color = 'blue', linestyle='dashed', label = "Minimum")
    plt.show()