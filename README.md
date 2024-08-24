# Extração de Tabelas de PDF e Geração de Planilha XLSX com Llama Parse

## 1 — Introdução

O objetivo deste projeto é extrair uma tabela de um arquivo PDF e gravar os dados em uma planilha no formato XLSX. Para a extração, utilizamos a API [Llama Parse](https://cloud.llamaindex.ai/).

O código do projeto está disponível no seguinte repositório: [extracao_pdf_com_ia](https://github.com/rodrigorocha1/extracao_pdf_com_ia).

## 2 — Fluxo do Processo

1. **Definição da Consulta:**
    - A primeira etapa do processo envolve a definição da consulta que a API irá interpretar. Para este projeto, a seguinte consulta foi utilizada:
    ```
    Este pdf contém tabelas com as colunas ITEM, PRODUTO, DESCRIÇÃO, QTD, UNIDADE, VALOR REF.
    
    Eu gostaria de obter as tabelas, use o separador |.
    
    Exemplo de como você deve separar: 
    coluna: ITEM|PRODUTO|DESCRIÇÃO|QTD|UNIDADE|VALOR REF. 
    Linha: 10|BORRACHA BRANCA|BORRACHA ESCOLAR, PARA APAGAR|1000|Caixas|11,26
    ```

2. **Extração e Tratamento de Dados:**
    - A resposta da API será tratada para garantir que os dados estejam devidamente formatados e prontos para serem gravados na planilha.

3. **Geração da Planilha XLSX:**
    - Após o tratamento dos dados, eles são salvos em um arquivo XLSX, organizados conforme a estrutura original da tabela extraída do PDF.

## 3 — Vídeo com Demonstração

Você pode assistir à demonstração do processo completo no vídeo a seguir:
[![Vídeo de Demonstração]](https://www.youtube.com/watch?v=HExBJzaeKzE)

