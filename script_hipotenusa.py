#!/usr/bin/env python3

# Importa o modulo sys para acessar os argumentos da linha de comando
import sys

# Confere se o usuario informou exatamente dois argumentos
if len(sys.argv) != 3:
    print("Erro: informe dois inteiros positivos, a e b, menores que 500.")
    sys.exit(1)

# Confere se os argumentos contem apenas digitos
if not sys.argv[1].isdigit() or not sys.argv[2].isdigit():
    print("Erro: os argumentos devem ser numeros inteiros positivos.")
    sys.exit(1)

# Converte os argumentos para inteiros
a = int(sys.argv[1])
b = int(sys.argv[2])

# Confere se os valores sao positivos e menores que 500
if not (0 < a < 500 and 0 < b < 500):
    print("Erro: a e b devem ser positivos e menores que 500.")
    sys.exit(1)

# Calcula o quadrado da hipotenusa
quadrado_hipotenusa = a**2 + b**2

# Imprime o resultado no formato solicitado
print(f"O quadrado da hipotenusa para o triangulo retângulo com lados a={a} e b={b}, é {quadrado_hipotenusa}")
