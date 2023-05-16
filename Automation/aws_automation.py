import boto3
import csv
import time
from reportlab.lib.pagesizes import landscape
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.lib import colors

# credenciais
access_key = "access_key"
secret_key = "secret_key"

# Cria uma nova instancia
iam_client = boto3.client(
    'iam',
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key
)

# Gera um novo relatorio
response = iam_client.generate_credential_report()

# Aguarda até o relatorio ser gerado
while True:
    try:
        report_response = iam_client.get_credential_report()
        if 'Content' in report_response:
            break
    except iam_client.exceptions.CredentialReportNotReadyException:
        print("Report is not yet ready. Waiting 5 seconds...")
        time.sleep(5)

# Decoda as strings UTF-8 se houverem
report_content = report_response['Content'].decode('utf-8')
rows = report_content.split('\n')

# Gera o CSV
csv_file_path = 'name.csv'
with open(csv_file_path, 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=rows[0].split(','))
    writer.writeheader()
    for row in rows[1:]:
        if row:
            writer.writerow(dict(zip(rows[0].split(','), row.split(','))))

# Gera o relatório PDF
pdf_file_path = 'name.pdf'

# seta o tamanho da pagina
page_width = 45 * inch
page_height = 10.5 * inch

doc = SimpleDocTemplate(pdf_file_path, pagesize=(page_width, page_height), leftMargin=0.5 * inch, rightMargin=0.5 * inch,
                        topMargin=0.5 * inch, bottomMargin=0.5 * inch)

# Define a largura da coluna
num_columns = len(rows[0].split(','))
col_widths = None  # Ajusta o tamanho da coluna automaticamente

table_data = [rows[0].split(',')] + [row.split(',') for row in rows[1:] if row]
table = Table(table_data, colWidths=col_widths, repeatRows=1)

# estilo da tabela
table.setStyle(
    [
        ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.wheat),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, 0), 10),  # seta o tamanho da fonte
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('GRID', (0, 0), (-1, -1), 1, colors.black),
    ]
)

elements = [table]
doc.build(elements)

# Mostra o nome do arquivo salvo
print("Credential report saved to:", pdf_file_path)
