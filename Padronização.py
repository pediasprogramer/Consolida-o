import os
import shutil
import openpyxl  # Biblioteca para ler arquivos Excel

# Configurações
pasta_origem = r'C:\Users\pedro.pneto\OneDrive - Ministério do Desenvolvimento e Assistência Social\Upload_Dados'
pasta_destino = r'C:\Users\pedro.pneto\OneDrive - Ministério do Desenvolvimento e Assistência Social\Padronização'
prefixo_nome = 'Planilha_Transferencia'

# Listar todos os arquivos Excel na pasta de origem
arquivos = [f for f in os.listdir(pasta_origem)
            if f.endswith(('.xlsx', '.xls')) and not f.startswith('~$')]


# Função para extrair o ano da coluna C (Nº Proposta)
def extrair_ano(caminho_arquivo):
    try:
        # Carrega o arquivo Excel
        wb = openpyxl.load_workbook(caminho_arquivo)
        sheet = wb.active  # Pega a primeira planilha

        # Percorre a coluna C até achar um valor no formato "xxxxx/ano"
        for row in sheet.iter_rows(min_col=3, max_col=3, values_only=True):
            if row[0] and isinstance(row[0], str) and '/' in row[0]:
                proposta = row[0].split('/')[-1]  # Pega o ano após a barra
                if proposta.isdigit() and len(proposta) == 4:  # Verifica se é um ano válido
                    return proposta
        return "DESCONHECIDO"  # Caso não encontre o padrão
    except Exception as e:
        print(f"Erro ao ler {caminho_arquivo}: {e}")
        return "ERRO"


# Processar cada arquivo
for arquivo in arquivos:
    caminho_origem = os.path.join(pasta_origem, arquivo)

    # Extrai o ano da proposta
    ano = extrair_ano(caminho_origem)

    # Define o novo nome
    nome_novo = f"{prefixo_nome}_{ano}.xlsx"
    caminho_destino = os.path.join(pasta_destino, nome_novo)

    # Evita sobrescrever arquivos existentes
    contador = 1
    while os.path.exists(caminho_destino):
        nome_novo = f"{prefixo_nome}_{ano}_{contador}.xlsx"
        caminho_destino = os.path.join(pasta_destino, nome_novo)
        contador += 1

    # Move o arquivo
    shutil.move(caminho_origem, caminho_destino)
    print(f"Arquivo {arquivo} renomeado para {nome_novo} e movido para {pasta_destino}")

print("Processo concluído!")