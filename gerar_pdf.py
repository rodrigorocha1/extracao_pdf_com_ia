from fpdf import FPDF

# Dados da tabela
dados = [
    ['Produto A', 'Descrição do Produto A', 'R$ 10,00'],
    ['Produto B', 'Descrição do Produto B', 'R$ 20,00'],
    ['Produto C', 'Descrição do Produto C', 'R$ 30,00']
] * 30  # Ajuste o número de repetições conforme necessário


class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 12)
        self.cell(0, 10, 'Tabela de Produtos', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Página {self.page_no()}', 0, 0, 'C')

    def table(self, header, data):
        self.set_font('Arial', 'B', 12)
        col_width = self.get_string_width(header[0])
        for item in header:
            col_width = max(col_width, self.get_string_width(item))
        col_width += 10

        self.cell(col_width, 10, header[0], 1)
        self.cell(col_width, 10, header[1], 1)
        self.cell(col_width, 10, header[2], 1)
        self.ln()

        self.set_font('Arial', '', 12)
        for row in data:
            self.cell(col_width, 10, row[0], 1)
            self.cell(col_width, 10, row[1], 1)
            self.cell(col_width, 10, row[2], 1)
            self.ln()


# Criar instância do PDF
pdf = PDF()
pdf.add_page()

# Número de linhas por página
linhas_por_pagina = 15  # Ajuste conforme necessário para caber na página

# Adicionar cada tabela em várias páginas
for i in range(0, len(dados), linhas_por_pagina):
    if i > 0:
        pdf.add_page()
    pdf.table(['NOME_PRODUTO', 'DESCRICAO', 'PRECO'],
              dados[i:i + linhas_por_pagina])

# Salvar o PDF
pdf.output('tabela_produtos_2_paginas.pdf')

print("PDF gerado com sucesso!")
