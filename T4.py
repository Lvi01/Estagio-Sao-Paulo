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
    
    Total = (SP + RJ + MG + 
                         ES + Outros)
    
    percentual_sp = Calcular(SP, Total)
    percentual_rj = Calcular(RJ, Total)
    percentual_mg = Calcular(MG, Total)
    percentual_es = Calcular(ES, Total)
    percentual_outros = Calcular(Outros, Total)
    
    print(f"Representacao de RJ: {percentual_rj:.2f}%")
    print(f"Representacao de SP: {percentual_sp:.2f}%")
    print(f"Representacao de MG: {percentual_mg:.2f}%")
    print(f"Representacao de ES: {percentual_es:.2f}%")
    print(f"Representacao de Outros: {percentual_outros:.2f}%")

if __name__ == "__main__":
    main()
