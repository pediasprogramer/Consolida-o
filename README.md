# Portfólio - Projeto de Consolidação e Padronização de Dados

Bem-vindo ao meu projeto pessoal desenvolvido em Python, focado em automação de tarefas de consolidação e padronização de dados. Este repositório demonstra minhas habilidades em manipulação de dados com `pandas`, extração de texto com `PyPDF2`, e organização de arquivos com bibliotecas como `os` e `shutil`. Criado por Pedro Neto em 21 de maio de 2025.

## Sobre o Projeto

Este projeto inclui três scripts que automatizam processos comuns em análise de dados:
- **Consolidação de Custos**: Junta dados de várias abas de um arquivo Excel.
- **Consolidação de Dados de PDF**: Extrai e organiza informações de PDFs em tabelas.
- **Padronização de Arquivos**: Renomeia e organiza arquivos Excel com base em metadados.

## Detalhes dos Scripts

### 1. Consolidação de Custos
- **Descrição**: Utiliza `pandas` para consolidar dados de múltiplas abas de um arquivo Excel, excluindo a aba "Código SIPEA", e gera um arquivo consolidado.
- **Imagem de Exemplo**:  
  ![Exemplo de Consolidação](https://i.imgur.com/tekDxYy.png)
- **Imagem de Resultado**:  
  ![Resultado da Consolidação](https://i.imgur.com/Y4NjqEL.png)

### 2. Consolidação de Dados de PDF
- **Descrição**: Extrai texto de PDFs com `PyPDF2`, processa dados (ID, nome, notas) usando expressões regulares, e exporta para Excel.
- **Imagem de Exemplo**:  
  ![Exemplo de Extração de PDF](https://i.imgur.com/1D95fzC.png)

### 3. Padronização de Arquivos
- **Descrição**: Organiza arquivos Excel, extrai anos de propostas, renomeia com prefixo e move para uma pasta de destino.
- **Imagem de Exemplo**:  
  ![Exemplo de Padronização](https://i.imgur.com/VhL0jBY.png)

## Habilidades Demonstradas
- Manipulação de dados com `pandas`.
- Extração de texto de PDFs com `PyPDF2`.
- Automação de tarefas com `os` e `shutil`.
- Uso de expressões regulares (`re`) para parsing de dados.
- Gestão de arquivos em Python.

## Pré-requisitos
- Python 3.x
- Bibliotecas: `pandas`, `PyPDF2`, `openpyxl`
- Instalação: pip install pandas PyPDF2 openpyxl
## Como Usar
1. Clone o repositório: git clone https://github.com/pediasprogramer/Consolida-o.git
2. 2. Ajuste os caminhos nos scripts (ex.: `caminho_arquivo`, `caminho_pdf`).
3. Execute os scripts:
python consolicao_Custo.py
python Consolidar_dados_de_PDF.py
python Padronizacao.py
## Contato
- **Autor**: Pedro Neto  
- **LinkedIn**: [https://www.linkedin.com/in/pedro-neto/]  
- **Email**: [pedro.pneto@esporte.com]  
- Sugestões ou melhorias? Abra uma issue!

## Licença
MIT License - Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

## Histórico de Atualizações
- **21/05/2025**: Criação inicial do projeto e documentação.
