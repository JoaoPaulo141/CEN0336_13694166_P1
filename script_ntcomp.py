
#!/usr/bin/env python3

# Solicita ao usuario uma sequencia de DNA
sequencia = input("Digite uma sequencia de DNA (A, T, C, G): ")

# Converte a sequencia para letras maiusculas
sequencia = sequencia.upper()

# Verificar se a sequencia contem apenas nucleotideos validos
if not sequencia or any(base not in "ATCG" for base in sequencia):
    print("Erro: digite uma sequencia contendo apenas A, T, C e G.")
else:
    # Inicializar a contagem de cada nucleotideo
    A = 0
    T = 0
    C = 0
    G = 0

    # Percorrer a sequencia e conta cada nucleotideo
    for base in sequencia:
        if base == "A":
            A += 1
        elif base == "T":
            T += 1
        elif base == "C":
            C += 1
        elif base == "G":
            G += 1

    # Exibir a quantidade de cada nucleotideo
    print(f"A: {A}")
    print(f"T: {T}")
    print(f"C: {C}")
    print(f"G: {G}")
