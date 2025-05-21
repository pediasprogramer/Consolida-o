import pandas as pd
import re
import PyPDF2

# Função para extrair texto do PDF
def extrair_texto_pdf(caminho_pdf):
    with open(caminho_pdf, 'rb') as file:
        leitor = PyPDF2.PdfReader(file)
        texto = ''
        for pagina in leitor.pages:
            texto += pagina.extract_text()
        return texto

# Função para processar os dados do texto extraído
def processar_dados_em_tabela(texto):
    # Padrão atualizado para capturar ID, nome e 6 notas (inclusive zeros)
    padrao = re.compile(
        r'(\d{8}),\s'                        # ID
        r'([^,]+(?: [^,]+)*?),\s'            # Nome (pode ter espaços e vírgulas)
        r'([\d.]+),\s'                       # Nota Redação
        r'([\d.]+),\s'                       # Matemática
        r'([\d.]+),\s'                       # Linguagens
        r'([\d.]+),\s'                       # Humanas
        r'([\d.]+),\s'                       # Natureza
        r'([\d.]+)'                          # Nota Final
    )

    resultados = padrao.findall(texto)

    colunas = ['ID', 'Nome', 'Redação', 'Matemática', 'Linguagens', 'Humanas', 'Natureza', 'Nota Final']
    df = pd.DataFrame(resultados, columns=colunas)

    # Convertendo notas para float
    for col in colunas[2:]:
        df[col] = pd.to_numeric(df[col], errors='coerce')  # Em caso de erro, define como NaN

    return df

# Caminho do seu PDF
caminho_pdf = r'C:\Users\pedro.pneto\Downloads\content.pdf'

# Execução
texto_extraido = extrair_texto_pdf(caminho_pdf)
df_resultado = processar_dados_em_tabela(texto_extraido)

# Exportando para Excel
saida_excel = r'C:\Users\pedro.pneto\Downloads\notas_enem_unb.xlsx'
df_resultado.to_excel(saida_excel, index=False)

print(f"Arquivo Excel criado com sucesso em:\n{saida_excel}")
