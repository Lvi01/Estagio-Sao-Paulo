#Levi Silva Freitas
#Funcao responsavel por calcular o percental de representacao
def Calcular(Estado, Total):
    return (Estado / Total) * 100

def main():
    SP = 67836.43
    RJ = 36678.66
    MG = 29229.88
    ES = 27165.48
    Outros = 19849.53
    
    Total = (SP + RJ + MG + ES + Outros)
    
    percentSP = Calcular(SP, Total)
    percentRJ = Calcular(RJ, Total)
    percentMG = Calcular(MG, Total)
    percentES = Calcular(ES, Total)
    percentOutros = Calcular(Outros, Total)
    
    print(f"Representacao de RJ: {percentRJ:.2f}%")
    print(f"Representacao de SP: {percentSP:.2f}%")
    print(f"Representacao de MG: {percentMG:.2f}%")
    print(f"Representacao de ES: {percentES:.2f}%")
    print(f"Representacao de Outros: {percentOutros:.2f}%")

if __name__ == "__main__":
    main()
