# Lista de combinações de valores de P e Q (verdadeiro ou falso)
valores = [(1, 1), (1, 0), (0, 1), (0, 0)]

# Exibe o cabeçalho da tabela com as proposições lógicas
print("\n=== PARTE 1: Tabela Verdade para P and !Q ===  ")
print(" P | Q | !Q | P and !Q ")
print("-" * 19)

# Loop para calcular e exibir o valor de cada proposição para cada combinação de P e Q
for p, q in valores:   
    # Negação de Q (não Q), 1 para verdadeiro e 0 para falso
    not_q = int(not q)
    
    # Conjunção entre P e !Q (P and !Q)
    p_and_not_q = int(p and not_q)
    
    # Exibe a linha da tabela com os resultados das proposições
    print(f" {p} | {q} |  {not_q}  |    {p_and_not_q} ")

# Linha de separação entre as tabelas
print("-" * 19)

# Lista de combinações de valores de P, Q e R
valores = [(1, 1, 1), (1, 1, 0), (1, 0, 1),
           (1, 0, 0), (0, 1, 1), (0, 1, 0),
           (0, 0, 1), (0, 0, 0)]

# Exibe o cabeçalho da tabela com as proposições lógicas envolvendo P, Q e R
print("\n=== PARTE 2: Tabela Verdade para (P or R) or (!Q and R) === ")
print("\n P | Q | R | !Q | P or R | !Q and R | (P or R) or (!Q and R) ")
print("-" * 53)

# Loop para calcular e exibir o valor de cada proposição para cada combinação de P, Q e R
for p, q, r in valores:   
    # Negação de Q (não Q), 1 para verdadeiro e 0 para falso
    not_q = int(not q)
    
    # Disjunção entre P e R (P or R)
    p_or_r = int(p or r)
    
    # Conjunção entre !Q e R (!Q and R)
    not_q_and_r = int(not_q and r)
    
    # Expressão complexa que é a disjunção entre P ou R e (!Q e R)
    complex_expression = int(p_or_r or not_q_and_r)

    # Exibe a linha da tabela com os resultados das proposições
    print(f" {p} | {q} | {r} |  {not_q}  |    {p_or_r}    |     {not_q_and_r}    |         {complex_expression}        ")

# Linha de separação entre as tabelas
print("-" * 53)

# Lista de combinações de valores de P, Q e R
valores = [(1, 1, 1), (1, 1, 0), (1, 0, 1),
           (1, 0, 0), (0, 1, 1), (0, 1, 0),
           (0, 0, 1)]

# Exibe o cabeçalho da tabela com as proposições lógicas mais complexas
print("\n=== PARTE 3: Tabela Verdade para (P or !Q) and (P and Q)) or ((P or R) or (!Q and R)) ===")
print("\n P | Q | R | !Q | P or !Q | P and Q | P or R | !Q and R | ((P or !Q) and (P and Q)) or ((P or R) or (!Q and R)) ")
print("-" * 100)

# Loop para calcular e exibir o valor de cada proposição para cada combinação de P, Q e R
for p, q, r in valores:   
    # Negação de Q (não Q), 1 para verdadeiro e 0 para falso
    not_q = int(not q)
    
    # Disjunção entre P e !Q (P or !Q)
    p_or_not_q = int(p or not q)
    
    # Conjunção entre P e Q (P and Q)
    p_and_q = int(p and q)
    
    # Disjunção entre P e R (P or R)
    p_or_r = int(p or r)
    
    # Conjunção entre !Q e R (!Q and R)
    not_q_and_r = int(not_q and r)
    
    # Expressão complexa que é uma combinação das disjunções e conjunções anteriores
    complex_expression = int((p_or_not_q and p_and_q) or (p_or_r or not_q_and_r))

    # Exibe a linha da tabela com os resultados das proposições
    print(f" {p} | {q} | {r} |  {not_q}  |    {p_or_not_q}    |    {p_and_q}    |   {p_or_r}  |   {not_q_and_r}   |    {complex_expression}    ")
