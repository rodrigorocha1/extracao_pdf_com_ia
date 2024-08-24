from openpyxl import Workbook
from src.operacao_dados.ioperacao_dados import IoperacaoDados
from llama_index.core.schema import Document
from openpyxl.styles import Alignment

import re
import os


class OperacaoDadosXLSX(IoperacaoDados[Document]):

    def __init__(self) -> None:
        self.__caminho_raiz = os.getcwd()
        self.__planilha = Workbook()
        self.__palanilha_ativa = self.__planilha.active
        self.__palanilha_ativa.title = 'Tabela Extraida'
        self.__linha_inicio = 1
        self.__largura_maxima = 0

    def gerar_dados(self, reposta_ia: Document):
        for chave, tabela in enumerate(reposta_ia):
            resultado = re.sub(r'\|\-\-\-.*\|\n', '', tabela.text)
            linhas = resultado.split('\n')
            linhas_tabela = linhas[1:]
            if chave == 0:
                cabecalho = linhas[0].strip('|').strip('.').split('|')
                self.__palanilha_ativa.append(cabecalho)
            for linha in linhas_tabela:
                linha_tabela = linha.strip('|').split('|')
                self.__palanilha_ativa.append(linha_tabela)

    def centralizar(self):

        for cell in self.__palanilha_ativa[self.__linha_inicio]:
            cell.alignment = Alignment(
                horizontal='center',
                vertical='center'
            )

    def realizar_espacamento_coluna(self):
        for coluna in self.__palanilha_ativa.columns:

            letra_coluna = coluna[0].column_letter
            for celula in coluna:
                try:

                    if celula.value:
                        largura_maxima = max(
                            self.__largura_maxima,

                            len(str(celula.value))
                        )
                except:
                    pass

            adjusted_width = largura_maxima + 2
            self.__palanilha_ativa.column_dimensions[letra_coluna].width = adjusted_width

    def salvar_dados(self):
        self.__planilha.save(os.path.join(
            self.__caminho_raiz, 'planilha_preco.xlsx'))
        self.__planilha.close()
