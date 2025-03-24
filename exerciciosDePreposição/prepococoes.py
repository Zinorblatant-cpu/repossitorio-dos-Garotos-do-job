# Lista de combinações de valores de P e Q (verdadeiro ou falso)

# ====================
# PARTE 1: Tabela Verdade para (P ∨ Q) ∧ (P ∧ Q)
# ====================

valores = [(1, 1), (1, 0), (0, 1), (0, 0)]

# Exibe o cabeçalho da tabela
print("\n=== PARTE 1: Tabela Verdade para (P ∨ Q) ∧ (P ∧ Q) ===")
print("  P  |  Q  |  P ∨ Q  |  P ∧ Q  | (P ∨ Q) ∧ (P ∧ Q) ")
print("-" * 50)

# Loop para calcular e exibir os valores das proposições
for p, q in valores:
    p_or_q = int(p or q)  # Disjunção de P e Q
    p_and_q = int(p and q)  # Conjunção de P e Q
    result = int(p_or_q and p_and_q)  # Conjunção final

    # Exibe a linha formatada da tabela
    print(f"  {p:^3} |  {q:^3} |   {p_or_q:^3}   |   {p_and_q:^3}   |        {result:^3}       ")

# Linha de separação entre as tabelas
print("-" * 19)

# ====================
# PARTE 2: Tabela Verdade para (P ∨ R) ∨ (¬Q ∧ R)
# ====================

valores = [
    (1, 1, 1), (1, 1, 0), (1, 0, 1),
    (1, 0, 0), (0, 1, 1), (0, 1, 0),
    (0, 0, 1), (0, 0, 0)
]

# Exibe o cabeçalho da tabela
print("\n=== PARTE 2: Tabela Verdade para (P ∨ R) ∨ (¬Q ∧ R) ===")
print("  P  |  Q  |  R  |  ¬Q  | P ∨ R | ¬Q ∧ R | (P ∨ R) ∨ (¬Q ∧ R) ")
print("-" * 65)

# Loop para calcular e exibir os valores das proposições
for p, q, r in valores:
    not_q = int(not q)  # Negação de Q
    p_or_r = int(p or r)  # Disjunção de P e R
    not_q_and_r = int(not_q and r)  # Conjunção de ¬Q e R
    result = int(p_or_r or not_q_and_r)  # Disjunção final

    # Exibe a linha formatada da tabela
    print(f"  {p:^3} |  {q:^3} |  {r:^3} |   {not_q:^3}  |   {p_or_r:^3}   |   {not_q_and_r:^3}  |       {result:^3}      ")

# Linha de separação entre as tabelas
print("-" * 53)

# ====================
# PARTE 3: Tabela Verdade para ((P ∨ ¬Q) ∧ (P ∧ Q)) ∨ ((P ∨ R) ∨ (¬Q ∧ R))
# ====================
valores = [
    (1, 1, 1), (1, 1, 0), (1, 0, 1),
    (1, 0, 0), (0, 1, 1), (0, 1, 0),
    (0, 0, 1), (0, 0, 0)
]

# Exibe o cabeçalho da tabela
print("\n=== PARTE 3: Tabela Verdade para ((P ∨ ¬Q) ∧ (P ∧ Q)) ∨ ((P ∨ R) ∨ (¬Q ∧ R)) ===")
print("  P  |  Q  |  R  |  ¬Q  | P ∨ ¬Q | P ∧ Q | P ∨ R | ¬Q ∧ R | ((P ∨ ¬Q) ∧ (P ∧ Q)) ∨ ((P ∨ R) ∨ (¬Q ∧ R)) ")
print("-" * 90)

# Loop para calcular e exibir os valores das proposições
for p, q, r in valores:
    not_q = int(not q)
    p_or_not_q = int(p or not_q)
    p_and_q = int(p and q)
    p_or_r = int(p or r)
    not_q_and_r = int(not_q and r)

    result = int(((p_or_not_q and p_and_q) or (p_or_r or not_q_and_r)))

    print(f"  {p:^3} |  {q:^3} |  {r:^3} |   {not_q:^3}  |   {p_or_not_q:^3}   |   {p_and_q:^3}   |   {p_or_r:^3}   |   {not_q_and_r:^3}   |        {result:^3}         ")
