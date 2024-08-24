from src.ia_pdf.iia_pdf import IIApdf
from typing import List
from dotenv import load_dotenv
from llama_parse import LlamaParse
import os


load_dotenv()


class IAPDF(IIApdf):

    def __init__(self, intrucao_ia: str) -> None:
        self.__caminho_base = os.getcwd()
        self.__caminho_pdf = os.path.join(self.__caminho_base, 'teste.pdf')
        self.__parse_ia = LlamaParse(
            result_type='markdown',
            parsing_instruction='Este pdf contem tabelas com as colunas ITEM, PRODUTO, DESCRIÇÃO, QTD, UNIDADE, VALOR REF.Eu gostaria de obter as tabelas, use o separador | '
        )

    def obter_texto(self) -> List:
        return self.__parse_ia.load_data(self.__caminho_pdf)
