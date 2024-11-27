import re
from collections import Counter

def calcular_pontuacao(senha):
    pontuacao = 0
    regras_extras = 0

    # Verificando se a senha tem pelo menos 8 caracteres
    if len(senha) < 8:
        print("Coloque mais caracteres.")
        return 0  # Retorna 0 para senhas com menos de 8 caracteres

    # Adições
    num_caracteres = len(senha)
    pontuacao += num_caracteres * 4  # Atende ao requisito de tamanho mínimo de 8 caracteres

    maiusculas = len(re.findall(r'[A-Z]', senha))  # Contagem de maiúsculas
    print(f'maiusculas: {maiusculas}')
    if maiusculas > 0:
        pontuacao += maiusculas * 2
        regras_extras += 1

    minusculas = len(re.findall(r'[a-z]', senha))  # Contagem de minúsculas
    print(f'minusculas: {minusculas}')
    if minusculas > 0:
        pontuacao += minusculas * 2
        regras_extras += 1

    numeros = len(re.findall(r'[0-9]', senha))  # Contagem de números
    print(f'numeros: {numeros}')
    if numeros > 0:
        pontuacao += numeros * 4
        regras_extras += 1

    simbolos = len(re.findall(r'[^a-zA-Z0-9]', senha))  # Contagem de símbolos
    print(f'simbolos: {simbolos}')
    if simbolos > 0:
        pontuacao += simbolos * 6
        regras_extras += 1

    numeros_simbolos_meio = len(re.findall(r'(?<=\w)[^\w](?=\w)', senha))  # Números e símbolos no meio da senha
    print(f'numeros simbolos meio: {numeros_simbolos_meio}')
    pontuacao += numeros_simbolos_meio * 2

    # Regra extra de comprimento mínimo
    if num_caracteres >= 8:
        regras_extras += 1

    pontuacao += regras_extras * 2  # Aumenta a pontuação conforme as regras extras atendidas

    # Deduções
    if senha.isalpha():  # Somente letras
        pontuacao -= len(senha)

    if senha.isdigit():  # Somente números
        pontuacao -= len(senha)

    # Contando caracteres repetidos (insensível ao case)
    contador = Counter(senha.lower())
    caracteres_repetidos = sum(count - 1 for count in contador.values() if count > 1)
    print(f'caracteres repetidos: {caracteres_repetidos}')
    pontuacao -= caracteres_repetidos

    # Maiúsculas repetidas consecutivamente
    maiusculas_repetidas = len(re.findall(r'[A-Z]{2,}', senha))
    print(f'maiusculas repetidas: {maiusculas_repetidas}')
    pontuacao -= maiusculas_repetidas * 2

    # Minúsculas repetidas consecutivamente
    minusculas_repetidas = len(re.findall(r'[a-z]{2,}', senha))
    print(f'minusculas repetidas: {minusculas_repetidas}')
    pontuacao -= minusculas_repetidas * 2

    # Números consecutivos
    numeros_consecutivos = len(re.findall(r'[0-9]{2,}', senha))
    print(f'numeros consecutivos: {numeros_consecutivos}')
    pontuacao -= numeros_consecutivos * 2

    # Sequências de letras (ex: abc)
    letras_sequenciais = len(re.findall(r'(?=([a-zA-Z]{3,}))', senha))
    print(f'letras sequenciais: {letras_sequenciais}')
    pontuacao -= (letras_sequenciais - 2) * 3 if letras_sequenciais > 3 else 0

    # Sequências de números (ex: 123)
    numeros_sequenciais = len(re.findall(r'(?=([0-9]{3,}))', senha))
    print(f'numeros sequenciais: {numeros_sequenciais}')
    pontuacao -= (numeros_sequenciais - 2) * 3 if numeros_sequenciais > 3 else 0

    # Sequências de símbolos (ex: !@#)
    simbolos_sequenciais = len(re.findall(r'(?=([^a-zA-Z0-9]{3,}))', senha))
    print(f'simbolos sequenciais: {simbolos_sequenciais}')
    pontuacao -= (simbolos_sequenciais - 2) * 3 if simbolos_sequenciais > 3 else 0

    return max(0, pontuacao)  # Garante que a pontuação não seja negativa

# Função para classificar a senha
def classificar_senha(pontuacao):
    if pontuacao < 20:
        return "Muito fraca"
    elif 20 <= pontuacao < 40:
        return "Fraca"
    elif 40 <= pontuacao < 60:
        return "Boa"
    elif 60 <= pontuacao < 80:
        return "Forte"
    else:
        return "Muito forte"

# Função principal
def main():
    senha = input("Digite a senha para avaliar: ")
    pontuacao = calcular_pontuacao(senha)
    
    if pontuacao == 0:  # Senha com menos de 8 caracteres
        print("A senha é muito fraca por não ter 8 caracteres.")
    else:
        classificacao = classificar_senha(pontuacao)
        print(f"Pontuação: {pontuacao}")
        print(f"A senha é: {classificacao}")

#Certificação
if __name__ == "__main__":
    main()
