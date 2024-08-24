from src.ia_pdf.ia_pdf import IAPDF


ia_pdf = IAPDF()


for documento in ia_pdf.obter_texto():
    print(documento)
