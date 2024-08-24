from src.ia_pdf.iia_pdf import IIApdf
from src.ia_pdf.ia_pdf import IAPDF
from src.operacao_dados.ioperacao_dados import IoperacaoDados
from src.operacao_dados.operacao_dados_xlsx import OperacaoDadosXLSX


class PipelineGeradorPdf():

    def __init__(self, servico_ia: IIApdf, operacao_dados: IoperacaoDados) -> None:
        self.__servico_ia = servico_ia
        self.__operacao_dados = operacao_dados

    def rodar_pipeline(self):
        resposta_ia = self.__servico_ia.obter_texto()
        self.__operacao_dados.gerar_dados(reposta_ia=resposta_ia)
        self.__operacao_dados.centralizar()
        self.__operacao_dados.realizar_espacamento_coluna()
        self.__operacao_dados.salvar_dados()


if __name__ == '__main__':
    pgg = PipelineGeradorPdf(
        servico_ia=IAPDF(
            intrucao_ia=""" 
    Este pdf contem tabelas com as colunas ITEM, PRODUTO, DESCRIÇÃO, QTD, UNIDADE, VALOR REF.
    Eu gostaria de obter as tabelas, use o separador |,
    Exemplo de como você deve separar: coluna: ITEM|PRODUTO|DESCRIÇÃO|QTD|UNIDADE|VALOR REF. Linha: 10|BORRACHA BRANCA|BORRACHA ESCOLAR, PARA APAGAR|1000| Caixas|11,26
    

"""),
        operacao_dados=OperacaoDadosXLSX()
    )
    pgg.rodar_pipeline()
