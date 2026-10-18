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


def maioria(texto):
    vogais = "aeiou"

    v = [letra for letra in texto if letra in vogais]
    c = [letra for letra in texto if letra not in vogais]

    if len(v) < len(c):
        return "".join(v)
    elif len(c) < len(v):
        return "".join(c)
    else:
        return "empate"

palavra = input("Digite uma palavra para cifrar: ").lower()
print(cifrar(palavra) + invert(palavra) + maioria(palavra))