#Levi Silva Freitas
#Resolvi utilizar a linguagem Python para resolver essa questao
#devido a sua facilidade de ler e interagir com arquivos externos.

import json

#Funcao responsavel por ler o arquivo json e guardar os seus dados
def ler_faturamento_json(filename):
    with open(filename, 'r') as file:
        data = json.load(file)
    faturamento = data.get("faturamento", [])
    return faturamento

#Funcao responsavel por identificar o maior e menor entre os valores
def calcular_menor_maior(faturamento):
    valores_validos = [valor for valor in faturamento if valor is not None]
    menor = min(valores_validos) if valores_validos else None
    maior = max(valores_validos) if valores_validos else None
    return menor, maior

#Funcao responsavel por calcular a media
def calcular_media(faturamento):
    valores_validos = [valor for valor in faturamento if valor is not None]
    if valores_validos:
        return sum(valores_validos) / len(valores_validos)
    return None

#Compara e verifica os dias que estao acima da media
def contar_dias_acima_media(faturamento, media):
    if media is None:
        return 0
    return sum(1 for valor in faturamento if valor is not None and valor > media)

def main():
    filename = 'faturamento.json'
    faturamento = ler_faturamento_json(filename)

    menor, maior = calcular_menor_maior(faturamento)
    media = calcular_media(faturamento)
    dias_acima_media = contar_dias_acima_media(faturamento, media)

    print(f"Menor valor de faturamento: {menor}")
    print(f"Maior valor de faturamento: {maior}")
    print(f"Media de valor de faturamento: {media}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

if __name__ == "__main__":
    main()
