import pandas as pd

"""
df1 = pd.read_excel("empregados1.xlsx")
df2 = pd.read_excel("empregados2.xlsx")
df3 = pd.read_excel("empregados3.xlsx")

todos_funcionarios = pd.concat([df1, df2, df3], ignore_index=True)
print(todos_funcionarios)
print()

#TP 3.3
quantidade_por_cargo = todos_funcionarios["cargo"].value_counts().reset_index()
quantidade_por_cargo.columns = ["cargo", "quantidade"]
print("Quantidade total de funcionários por cargo:")
print(quantidade_por_cargo)
print()

#TP 3.4
cargo_mais_comum = quantidade_por_cargo.iloc[0]
print(f"Cargo com mais funcionários: {cargo_mais_comum['cargo']} - ({cargo_mais_comum['quantidade']} funcionários)")

# TP 3.5
def classificar_cargo(cargo):
    cargo = str(cargo).lower()
    
    if cargo.startswith(("c", "supervisor", "coordenador")):
        return "Alto"
    elif cargo.startswith(("estagiário", "assistente", "analista")):
        return "Baixo"
    else:
        return "Médio"
    
todos_funcionarios["classificacao"] = todos_funcionarios["cargo"].apply(classificar_cargo)
print("Funcionários com classificação de cargos:")
print(todos_funcionarios)
print()

#TP 3.6
resumo_funcionarios = todos_funcionarios.merge(quantidade_por_cargo, on="cargo", how="left")
resumo_funcionarios.to_excel("resumo_funcionarios.xlsx", index=False)
print("Resumo salvo em resumo_funcionarios.xlsx")
print()
"""

#TP 3.7
projetos = pd.read_excel("projetos.xlsx")

print("Estrutura da tabela projetos:")
print(projetos.info())
print()

#TP 3.8
novos_projetos = pd.DataFrame({"projetoID": [104, 105, 106], "nome_projeto": ["Projeto XYZ", "Desenvolvimento Tardio", "Projeto Legal"], "prazo": ["2025-04-13", "2025-03-17", "2025-05-26"]})
with pd.ExcelWriter("projetos.xlsx", mode='a', engine='openpyxl', if_sheet_exists='overlay') as writer:
    novos_projetos.to_excel(writer, sheet_name='Planilha1', header=False, index=False, startrow=len(projetos) + 1)
print(projetos)
print()

#TP 3.9
novo_prazo = projetos.loc[projetos["nome_projeto"] == "Sistema X", "prazo"] = "2025-12-31"
print(projetos)
print()

#TP 3.10
projetos['prazo'] = pd.to_datetime(projetos['prazo'])
projetos = projetos.loc[projetos['prazo'] > pd.to_datetime('today')]
print(projetos)
print()