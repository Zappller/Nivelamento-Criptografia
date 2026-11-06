import numpy as np

alfabeto = "abcdefghijklmnopqrstuvwxyz"
tabela = np.array([list(alfabeto[i:] + alfabeto[:i]) for i in range(26)])

def cifrar(texto):
    chave = "artyom"
    resultado = ""

    for k, letra in enumerate(texto):
        i = alfabeto.index(chave[k % len(chave)])   
        j = alfabeto.index(letra)                  
        resultado += tabela[i, j]

    return resultado

def invert(texto):
    if len(texto) <=3:
        return texto
    else:
        resultado2 = texto[0] + texto[1:-1][::-1] + texto[-1]
        return resultado2


def eh_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def maioria(palavra):
    vogais = "aeiou"
    primo = eh_primo(len(palavra))
    resultado = ""

    for letra in palavra:
        e_vogal = letra in vogais

        if primo and not e_vogal:
            resultado += letra
        if not primo and e_vogal:
            resultado += letra

    return resultado

palavra = input("Digite uma palavra para cifrar: ").lower()
print(cifrar(palavra) + invert(palavra) + maioria(palavra))