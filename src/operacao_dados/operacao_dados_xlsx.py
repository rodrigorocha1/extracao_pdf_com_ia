from openpyxl import Workbook
from src.operacao_dados.ioperacao_dados import IoperacaoDados
from llama_index.core.schema import Document
import re
import os


class OperacaoDadosXLSX(IoperacaoDados[Document]):

    def __init__(self) -> None:
        self.__caminho_raiz = os.getcwd()
        self.__planilha = Workbook()
        self.__palanilha_ativa = self.__planilha.active
        self.__planilha.active = 'Tabela Extraida'

    def gerar_dados(self, reposta_ia: Document):
        for chave, tabela in enumerate(reposta_ia):
            texto_sem_separadores_orig = re.sub(
                r'^\|---\|---\|---\|---\|---\|---\|\s*\n?', '', tabela.text, flags=re.MULTILINE)
            texto_sem_separadores = texto_sem_separadores_orig.split('\n')
            colunas = [[item for item in coluna.split(
                '|') if item.strip()] for coluna in texto_sem_separadores]
            cabecalho, *linhas = colunas
            if chave == 0:
                self.__palanilha_ativa.append(cabecalho)
            else:
                for linha in linhas:
                    self.__palanilha_ativa.append(linha)

    def salvar_dados(self):
        self.__planilha.save(os.path.join(
            self.__caminho_raiz, 'planilha_preco.xlsx'))
        self.__planilha.close()
