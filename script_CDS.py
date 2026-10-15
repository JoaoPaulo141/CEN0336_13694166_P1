
#!/usr/bin/env python3

# Importar o modulo sys para acessar os argumentos da linha de comando
import sys

# Verificar se foram fornecidos sete argumentos
if len(sys.argv) != 8:
    print("Erro: informe a sequencia de DNA e seis coordenadas.")
    sys.exit(1)

# Receber a sequencia de DNA e verificar se e uma string
sequencia = sys.argv[1]

if not isinstance(sequencia, str):
    print("Erro: a sequencia de DNA deve ser uma string.")
    sys.exit(1)

# Verificar se as seis coordenadas sao numeros inteiros positivos
argumentos = sys.argv[2:]

for argumento in argumentos:
    if not argumento.isdigit():
        print("Erro: as coordenadas devem ser numeros inteiros positivos.")
        sys.exit(1)

# Converter as coordenadas de string para inteiros
n1, n2, n3, n4, n5, n6 = map(int, argumentos)

# Verificar se nenhuma coordenada excede o tamanho da sequencia
for n in (n1, n2, n3, n4, n5, n6):
    if n > len(sequencia):
        print("Erro: uma coordenada excede o tamanho da sequencia.")
        sys.exit(1)

# Verificar se as coordenadas estao em ordem crescente
if not (n1 < n2 < n3 < n4 < n5 < n6):
    print("Erro: as coordenadas devem estar em ordem crescente.")
    sys.exit(1)

# Extrair as tres regioes codificantes (CDS)
cds1 = sequencia[:n2]
cds2 = sequencia[n3-1:n4]
cds3 = sequencia[n5-1:n6]

# Extrair os dois introns
intron1 = sequencia[n2:n3-1]
intron2 = sequencia[n4:n5-1]

# Verificar se o primeiro intron comeca com GT e termina com AG
if intron1.startswith("GT") and intron1.endswith("AG"):

# Verificar se o segundo intron comeca com GT e termina com AG
    if intron2.startswith("GT") and intron2.endswith("AG"):

    # Concatenar e imprimir as tres CDS
        sequencia_cds = cds1 + cds2 + cds3
        print(sequencia_cds)

    else:
        print("Erro: o intron 2 nao comeca com GT ou nao termina com AG.")

else:
    print("Erro: o intron 1 nao comeca com GT ou nao termina com AG.")
