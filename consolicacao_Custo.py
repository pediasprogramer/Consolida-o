import pandas as pd

# Caminho do arquivo
caminho_arquivo = r'C:\Users\pedro.pneto\Downloads\Preços do Esporte Amador.xlsx'

# Lista todas as abas do arquivo, exceto "Código SIPEA"
abas = pd.ExcelFile(caminho_arquivo).sheet_names
abas_para_consolidar = [aba for aba in abas if aba != "Código SIPEA"]

# Lista para armazenar os DataFrames de cada aba
dfs = []

# Ler cada aba e adicionar à lista
for aba in abas_para_consolidar:
    df = pd.read_excel(caminho_arquivo, sheet_name=aba)
    df['Origem'] = aba  # Adiciona coluna indicando a origem
    dfs.append(df)

# Consolidar todos os DataFrames
consolidado = pd.concat(dfs, ignore_index=True)

# Salvar o resultado em um novo arquivo Excel
caminho_saida = r'C:\Users\pedro.pneto\Downloads\Consolidado_Preços_Esporte_Amador.xlsx'
consolidado.to_excel(caminho_saida, index=False)

print(f"Consolidação concluída! Arquivo salvo em: {caminho_saida}")