import re

def calcular_pontuacao(senha):
    pontuacao = 0
    regras_extras = 0

    # Adições
    num_caracteres = len(senha)
    pontuacao += num_caracteres * 4

    maiusculas = len(re.findall(r'[A-Z]', senha))
    if maiusculas > 0:
        pontuacao += (num_caracteres - maiusculas) * 2
        regras_extras += 1

    minusculas = len(re.findall(r'[a-z]', senha))
    if minusculas > 0:
        pontuacao += (num_caracteres - minusculas) * 2
        regras_extras += 1

    numeros = len(re.findall(r'[0-9]', senha))
    if numeros > 0:
        pontuacao += numeros * 4
        regras_extras += 1

    simbolos = len(re.findall(r'[^a-zA-Z0-9]', senha))
    if simbolos > 0:
        pontuacao += simbolos * 6
        regras_extras += 1

    numeros_simbolos_meio = len(re.findall(r'(?<=[a-zA-Z]).(?=[a-zA-Z])', senha))
    pontuacao += numeros_simbolos_meio * 2

    # Regra extra de comprimento mínimo
    if num_caracteres >= 8:
        regras_extras += 1

    pontuacao += regras_extras * 2

    # Deduções
    if senha.isalpha():
        pontuacao -= len(senha)

    if senha.isdigit():
        pontuacao -= len(senha)

    caracteres_repetidos = len(senha) - len(set(senha.lower()))
    pontuacao -= caracteres_repetidos

    maiusculas_repetidas = len(re.findall(r'[A-Z]{2,}', senha))
    pontuacao -= maiusculas_repetidas * 2

    minusculas_repetidas = len(re.findall(r'[a-z]{2,}', senha))
    pontuacao -= minusculas_repetidas * 2

    numeros_consecutivos = len(re.findall(r'[0-9]{2,}', senha))
    pontuacao -= numeros_consecutivos * 2

    letras_sequenciais = len(re.findall(r'(?=([a-zA-Z]{3,}))', senha))
    pontuacao -= (letras_sequenciais - 2) * 3 if letras_sequenciais > 3 else 0

    numeros_sequenciais = len(re.findall(r'(?=([0-9]{3,}))', senha))
    pontuacao -= (numeros_sequenciais - 2) * 3 if numeros_sequenciais > 3 else 0

    simbolos_sequenciais = len(re.findall(r'(?=([^a-zA-Z0-9]{3,}))', senha))
    pontuacao -= (simbolos_sequenciais - 2) * 3 if simbolos_sequenciais > 3 else 0

    return max(0, pontuacao)

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

def main():
    senha = input("Digite a senha para avaliar: ")
    pontuacao = calcular_pontuacao(senha)
    classificacao = classificar_senha(pontuacao)

    print(f"Pontuação: {pontuacao}")
    print(f"A senha é: {classificacao}")

if __name__ == "__main__":
    main()
