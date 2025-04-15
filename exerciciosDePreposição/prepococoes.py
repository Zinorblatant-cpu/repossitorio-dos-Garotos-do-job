
# Exibe o cabeçalho da tabela com as proposições lógicas
print("\n=== PARTE 1: Tabela Verdade para P and !Q ===  ")
print(" P | Q | !Q | P and !Q ")
print("-" * 19)

# Loop para calcular e exibir o valor de cada proposição para cada combinação de P e Q
for p in range(2):
    for q in range(2):
        not_q = int(not q)  # Calcula a negação de Q
        output = int(p and not_q)  # Avalia P and !Q
        print(f" {p} | {q} |  {not_q}  |    {output} ")

# Linha de separação entre as tabelas
print("-" * 19)

# Exibe o cabeçalho da tabela com as proposições lógicas envolvendo P, Q e R
print("\n=== PARTE 2: Tabela Verdade para (P or R) or (!Q and R) === ")
print("\n P | Q | R | !Q | P or R | !Q and R | (P or R) or (!Q and R) ")
print("-" * 53)

# Loop para calcular e exibir o valor de cada proposição para cada combinação de P, Q e R
for p in range(2):   
    for q in range(2):
        for r in range(2):
            output = 0
            not_q = int(not q)
            p_or_r = int(p or r)
            not_q_and_r = int(not_q and r)
            if (p or r) or (not_q and r):
                output = 1
            # Exibe a linha da tabela com os resultados das proposições
            print(f" {p} | {q} | {r} |  {not_q}  |    {p_or_r}    |     {not_q_and_r}    |         {output}        ")

# Linha de separação entre as tabelas
print("-" * 53)

# Lista de combinações de valores de P, Q e R

# Exibe o cabeçalho da tabela com as proposições lógicas mais complexas
print("\n=== PARTE 3: Tabela Verdade para (P or !Q) and (P and Q)) or ((P or R) or (!Q and R)) ===")
print("\n P | Q | R | !Q | P or !Q | P and Q | P or R | !Q and R | ((P or !Q) and (P and Q)) or ((P or R) or (!Q and R)) ")
print("-" * 100)

# Loop para calcular e exibir o valor de cada proposição para cada combinação de P, Q e R
for p in range(2):   
    for q in range(2):
        for r in range(2):
            output = 0
            not_q = int(not q)
            p_or_not_q = int(p or not q)
            p_and_q = int(p and q)
            p_or_r = int(p or r)
            not_q_and_r = int(not_q and r)
            if ((p or not_q) and (p and q)) or ((p or r) or (not_q and r)):
                output = 1
            # Exibe a linha da tabela com os resultados das proposições
            print(f" {p} | {q} | {r} |  {not_q}  |    {p_or_not_q}    |    {p_and_q}    |   {p_or_r}  |   {not_q_and_r}   |    {output}    ")